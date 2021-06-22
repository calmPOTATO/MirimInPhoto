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

  dates.forEach((date, i) => {
    const condition = i >= firstDateIndex && i < lastDateIndex + 1
                      ? 'this'
                      : 'other';
    if(condition == 'other'){
      dates[i] = `<div class="date"><span class=${condition}>${date}</span></div>`;
    }else{
      dates[i] = `<div class="date"><span class=${condition}>${date}</span></div>`;
      $(".dates").click (function(){
        var click_date = $(event.target);
        click_date = click_date.text();
        $( 'h1' ).text( click_date );

        var click_month = "";
        var click_day = "";

        if(viewMonth+1<10) {
            click_month = "0"+String(viewMonth+1);
        } else {
            click_month = String(viewMonth+1);
        }

        if(click_date<10) {
            click_day = "0"+String(click_date);
        } else {
            click_day = String(click_date);
        }

        document.getElementById("select_date").value=String(viewYear)+""+click_month+""+click_day;

        var user_click = $('h1').text();
        if(date == user_click){
          $('h2').text(viewMonth+1 + "월  " + user_click + "일");
        }
      });
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