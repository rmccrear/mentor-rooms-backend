
function buildTable (taData) {
  let table = `
    <tr>
      <th>
        Mentor
      </th>
      <th>
        Meet link
      </th>
      <th>
        Mentor Available
      </th>
      <th>
        Room Full
      </th>
    </tr>
    `;
  for(const ta of taData) {
    table += `
      <tr>
        <td>
          ${ta.displayName}
        </td>
        <td>
          ${(ta.availableNow && !ta.roomFull && ta.meetLink) ?
                   `<a href="${ta.meetLink}"> ${ta.meetLink} </a>`
                   : "<span class='link-unavailable'></span>"}
        </td>
        <td>
          ${ta.availableNow ? 
                   "<span class='ta-available'></span>"
                   : "<span class='ta-unavailable'></span>"
          }
        </td>
        <td>
          ${(ta.availableNow && ta.meetLink) ? 
                   (ta.roomFull ? 
                   "<span class='ta-roomFull'></span>"
                   : "<span class='ta-roomNotFull'></span>")
            : "<span class='link-unavailable'></span>"
          }
        </td>

      </tr>
    `;
  }
  return table;
}

function getRealtimeData() {
  // let url = 'https://mentors-table-rmccrear.replit.app/get-status';
  let url = '/get-status';
  return fetch(url)
    .then((response) => response.json())
    .then(json => {
    // Do something with the data
    console.log(json);
    return json;
  });
}



const mentorTable = document.getElementById("mentors-table");

getRealtimeData().then((taData) => {
  console.log(taData);
  mentorTable.innerHTML = buildTable(taData);
})