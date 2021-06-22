let date = new Date();

const renderCalender = () => {
  const viewYear = date.getFullYear();
  const viewMonth = date.getMonth();

  document.querySelector('.year-month').textContent = `${viewMonth + 1}월`;

  const prevLast = new Date(viewYear, viewMonth, 0);
  const thisLast = new Date(viewYear, viewMonth + 1, 0);

  const PLDate = prevLast.getDate();
  const PLDay = prevLast.getDay();

  const TLDate = thisLast.getDate();
  const TLDay = thisLast.getDay();

  const prevDates = [];
  const thisDates = [...Array(TLDate + 1).keys()].slice(1);
  const nextDates = [];

  if (PLDay !== 6) {
    for (let i = 0; i < PLDay + 1; i++) {
      prevDates.unshift(PLDate - i);
    }
  }

  for (let i = 1; i < 7 - TLDay; i++) {
    nextDates.push(i);
  }

  const dates = prevDates.concat(thisDates, nextDates);
  const firstDateIndex = dates.indexOf(1);
  const lastDateIndex = dates.lastIndexOf(TLDate);

  const prev_date = document.getElementById('date').innerText;
  const result_date = new Date(prev_date.replace(/([\[\]])/g, ""));

  dates.forEach((date, i) => {
    const condition = i >= firstDateIndex && i < lastDateIndex + 1
                      ? 'this'
                      : 'other';
    if(condition == 'other'){
        dates[i] = `<div class="date"><span class=${condition}>${date}</span></div>`;
    }
    else{
        dates[i] = `<div class="date"><span class=${condition}>${date}</span></div>`;
        if(date == result_date.getDate() && viewMonth == result_date.getMonth()){
            switch(getParam()){
            case "전해원":
                dates[i] = `<div class="date"><span class=${condition}>${date}</span><div class="circle" style="background-color:#91C2C6"></div></div>`;
                break;
            case "성진민":
                dates[i] = `<div class="date"><span class=${condition}>${date}</span><div class="circle" style="background-color:#FFCCB6"></div></div>`;
                break;
            case "이서연":
                dates[i] = `<div class="date"><span class=${condition}>${date}</span><div class="circle" style="background-color:#FEE1E8"></div></div>`;
                break;
            case "이예서":
                dates[i] = `<div class="date"><span class=${condition}>${date}</span><div class="circle" style="background-color:#C6DBE1"></div></div>`;
                break;
            case "한나래":
                dates[i] = `<div class="date"><span class=${condition}>${date}</span><div class="circle" style="background-color:#80B3B3"></div></div>`;
                break;
            case "최민서":
                dates[i] = `<div class="date"><span class=${condition}>${date}</span><div class="circle" style="background-color:#D4F0F0"></div></div>`;
                break;
            case "김정미":
                dates[i] = `<div class="date"><span class=${condition}>${date}</span><div class="circle" style="background-color:#CBAACB"></div></div>`;
                break;
            case "유예영":
                dates[i] = `<div class="date"><span class=${condition}>${date}</span><div class="circle" style="background-color:#D79DAD"></div></div>`;
                break;
            case "안세은":
                dates[i] = `<div class="date"><span class=${condition}>${date}</span><div class="circle" style="background-color:#D9E6C3"></div></div>`;
                break;
            case "하사엘":
                dates[i] = `<div class="date"><span class=${condition}>${date}</span><div class="circle" style="background-color:#FF9AA2"></div></div>`;
                break;
            case "김바다":
                dates[i] = `<div class="date"><span class=${condition}>${date}</span><div class="circle" style="background-color:#FCB9AA"></div></div>`;
                break;

            default:
                break;
            }
        }
        else{
            dates[i] = `<div class="date"><span class=${condition}>${date}</span></div>`;
        }
    }
  });

  document.querySelector('.dates').innerHTML = dates.join('');

  const today = new Date();
  if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
    for (let date of document.querySelectorAll('.this')) {
      if (+date.innerText === today.getDate()) {
        date.classList.add('today');
        break;
      }
    }
  }
};

renderCalender();

function getParam(){
    var url = location.search;
    url = url.substring(14, 41);
    url = decodeURIComponent(url)

    return url;
}

const prevMonth = () => {
  date.setMonth(date.getMonth() - 1);
  renderCalender();
};

const nextMonth = () => {
  date.setMonth(date.getMonth() + 1);
  renderCalender();
};

const goToday = () => {
  date = new Date();
  renderCalender();
};