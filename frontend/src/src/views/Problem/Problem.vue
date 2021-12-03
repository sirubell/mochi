<template>
  <div>
    <div id="problem">
      <h1>This is a problem page</h1>
      <h1><router-link to="/problem/new">Add question</router-link></h1>
      <h1><router-link to="/problem/problem_id">題目標題</router-link></h1>
    </div>
    <div id="table"></div>
    <!-- <vue-json-to-table :data="jArray"></vue-json-to-table> -->
    
  </div>
</template>

<script type="text/javascript">


let jArray = 
[               
    {"problem_id":1,"problem_name":"Add","complexity":"hard"}, 
    {"problem_id":2,"problem_name":"Hello","complexity":"easy"}, 
    {"problem_id":3,"problem_name":"World","complexity":"hard"}, 
    {"problem_id":4,"problem_name":"times","complexity":"easy"}, 
    {"problem_id":5,"problem_name":"daily","complexity":"easy"}, 
    {"problem_id":6,"problem_name":"divide","complexity":"medium"}, 
    {"problem_id":7,"problem_name":"minus","complexity":"hard"}, 
    {"problem_id":8,"problem_name":"hey","complexity":"easy"}, 
];

function generateTable (jArray) {
    let tbody = document.createElement('tbody');
    let thead = document.createElement('thead');
    let table = document.createElement('table');
    jArray.forEach(row => {
        let tr = document.createElement('tr');

        Object.keys(row).forEach(tdName => {
            let td = document.createElement('td');
            td.textContent= row[tdName];

            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    let headerTr = document.createElement('tr')

    Object.keys(jArray[0]).forEach(header => {
        let th = document.createElement('th')
        th.textContent = header

        headerTr.appendChild(th)
    });
    thead.appendChild(headerTr);
    table.appendChild(thead);

    return table;
}

document.body.appendChild(generateTable(jArray));

</script>

<style>
#problem {
  text-align: center;
  vertical-align: center;
  font-size: 25px;
  line-height: 50px;
  letter-spacing: 4px;
}
</style>
