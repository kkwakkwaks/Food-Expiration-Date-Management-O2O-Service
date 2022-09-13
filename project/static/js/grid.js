// const gridData = [
//     {
//       category: '신선란',
//       name: '계란',
//       type: 'D-60',
//       release: '22.10.30',
//       genre: '22/10/30'
//     }
// ];

const grid = new tui.Grid({
    el: document.getElementById('grid'),
    data: gridData,
    scrollX: false,
    scrollY: false,
    columns: [
      {
        header: '소분류',
        name: 'subclass'
      },
      {
        header: '제품명',
        name: 'product'
      },
      {
        header: '남은일수',
        name: 'remain_date'
      },
      {
        header: '유통기한',
        name: 'old_exp_date'
      },
      {
        header: '소비기한',
        name: 'new_exp_date'
      }
    ]
  });
