let page_numbers = [
  1,
  2,
  3,
];

let current_page = 1;

let current_range = [
  (current_page - 1) * 5,
  ((current_page - 1) * 5) + 4
]

colors = [
  'Black_Gesso',
  'Bright_Red',
  'Burnt_Umber',
  'Cadmium_Yellow',
  'Dark_Sienna',
  'Indian_Red',
  'Indian_Yellow',
  'Liquid_Black',
  'Liquid_Clear',
  'Midnight_Black',
  'Phthalo_Blue',
  'Phthalo_Green',
  'Prussian_Blue',
  'Sap_Green',
  'Titanium_White',
  'Van_Dyke_Brown',
  'Yellow_Ochre',
  'Alizarin_Crimson',
];

subject_matter = [
  "AURORA_BOREALIS",
  "BARN",
  "BEACH",
  "BOAT",
  "BUILDING",
  "BUSHES",
  "CABIN",
  "CLIFF",
  "CLOUDS",
  "CONIFER",
  "CUMULUS",
  "DOCK",
  "FARM",
  "FENCE",
  "FIRE",
  "FLOWERS",
  "FOG",
  "GRASS",
  "HILLS",
  "LAKE",
  "LAKES",
  "LIGHTHOUSE",
  "MILL",
  "MOON",
  "MOUNTAIN",
  "MOUNTAINS",
  "NIGHT",
  "OCEAN",
  "PALM_TREES",
  "PATH",
  "PERSON",
  "RIVER",
  "ROCKS",
  "SNOW",
  "SNOWY_MOUNTAIN",
  "STRUCTURE",
  "SUN",
  "TREE",
  "WATERFALL",
  "WAVES",
  "WINDMILL",
  "WINTER",
];

seasons = [
  "Winter",
  "Spring",
  "Summer",
  "Fall",
];

async function Submit() {
  let checked;
  let user_selected_subject_matter = [];
  let user_selectd_colors = [];
  let user_selected_seasons = [];
  let i;
  page_numbers = [
    1,
    2,
    3,
  ];
  current_page = 1;
  current_range = [
    (current_page - 1) * 5,
    ((current_page - 1) * 5) + 4
  ]
  for (i = 1; i < 43; i++) {
    checked = document.querySelector(`.subject_matter #check-${i}`).checked;
    if (checked) {
      user_selected_subject_matter.push(subject_matter[i - 1])
    }
  }
  for (i = 1; i < 19; i++) {
    checked = document.querySelector(`.colors_used #check-${i}`).checked;
    if (checked) {
      user_selectd_colors.push(colors[i - 1])
    }
  }
  for (i = 1; i < 5; i++) {
    checked = document.querySelector(`.seasons #check-${i}`).checked;
    if (checked) {
      user_selected_seasons.push(seasons[i - 1])
    }
  }
  
  let color_episodes = $.ajax({
    async: false,
    type: "POST",
    url: 'https://fvo6q7f166.execute-api.us-east-1.amazonaws.com/beta/colors_used',
    data: JSON.stringify(user_selectd_colors),
    success: (data) => {
      console.log('success');
    },
    dataType: 'json'
  }).responseJSON.body;

  let subject_matter_episodes = $.ajax({
    async: false,
    type: "POST",
    url: 'https://fvo6q7f166.execute-api.us-east-1.amazonaws.com/beta/subject_matter',
    data: JSON.stringify(user_selected_subject_matter),
    success: (data) => {
      console.log('success');
    },
    dataType: 'json'
  }).responseJSON.body;

  let season_episodes = $.ajax({
    async: false,
    type: "POST",
    url: 'https://fvo6q7f166.execute-api.us-east-1.amazonaws.com/beta/seasons',
    data: JSON.stringify(user_selected_seasons),
    success: (data) => {
      console.log('success');
    },
    dataType: 'json'
  }).responseJSON.body;
  episodes_to_show = {};
  for (const episode in subject_matter_episodes) {
    if (user_selectd_colors.length + user_selected_seasons.length + user_selected_subject_matter.length === 0) {
      episodes_to_show = color_episodes;
      break;
    }
    if ((episode in season_episodes) && (episode in color_episodes)) {
      episodes_to_show[episode] = subject_matter_episodes[episode];
    }
  }
  display_videos(episodes_to_show);
}

function display_videos(episodes_to_show) {
  remove_results();
  display_pagination(Object.keys(episodes_to_show).length);

  let i = 0;
  let j = 0;
  let start_point = current_range[0];
  let end_point = current_range[1];
  $(".hits").append(`<h3>Total hits: ${Object.keys(episodes_to_show).length}<h3>`);
  for (const episode in episodes_to_show) {
    if (j === 5) {
      break;
    }
    if (i >= start_point && i <= end_point) {
      $(".results-section").append(`
        <div class="card youtube-video m-auto" style="width: 18rem;">
          <iframe  src="${episodes_to_show[episode]}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          <div class="card-body">
            <h5 class="card-title">${episode}</h5>
          </div>
        </div>
      `);
      j++;
    }
    i++;
  }
}

function remove_results() {
  const results = document.getElementsByClassName("results-section")[0];
  results.innerHTML = '';
  remove_pagination();
}

function remove_pagination() {
  const pagination = document.getElementsByClassName("pagination-section")[0];
  pagination.innerHTML = '';
  const hits = document.getElementsByClassName("hits")[0];
  hits.innerHTML = '';
}

function display_pagination(total) {
  let total_num_pages = Math.ceil(total / 5);

  $('.pagination-section').append(`
    <nav aria-label="Page navigation example">
      <ul class="page-numbers pagination">
        
      </ul>
    </nav>
  `)
  for (let i = 0; i < 3; i++) {
    if (i === 1) {
      $('.page-numbers').append(`
      <li class="page-item"><a id="p-${page_numbers[i]}" class="page-link" value="${i + 1}">${current_page}</a></li>
    `);
    } else if (i === 0) {
      $('.page-numbers').append(`
        <li class="page-item"><a id="p-${page_numbers[i]}" class="page-link" value="${i + 1}">prev</a></li>
      `);
    } else {
      $('.page-numbers').append(`
      <li class="page-item"><a id="p-${page_numbers[i]}" class="page-link" value="${i + 1}">next</a></li>
    `);
    }
    $(`.page-numbers #p-${page_numbers[i]}`).on("click", function() {
      if (current_page === page_numbers[i] && current_page < 1) {
        return 1;
      }
      if (current_page === 1) {
        current_page = 2;
      } else {
        current_page = page_numbers[i];
      }
      current_range[0] = (current_page - 1) * 5;
      current_range[1] = current_range[0] + 4;
      // alert(`current Page ${current_page} ${current_range[0]}:${current_range[1]}`)
      if (current_page === 1) {
        page_numbers[0] = 1;
        page_numbers[1] = 2;
        page_numbers[2] = 3;
      } else if (current_page === total_num_pages) {
        page_numbers[0] = current_page - 2;
        page_numbers[1] = current_page - 1;
        page_numbers[2] = current_page;
      } else {
        page_numbers[0] = current_page - 1;
        page_numbers[1] = current_page;
        page_numbers[2] = current_page + 1;
      }
      remove_pagination();
      display_pagination(Object.keys(episodes_to_show).length);
      display_videos(episodes_to_show);
    })
  }
}
