var hh = 0;
var mm = 0;
var ss = 0;

var tempo = 1000;
var cron;
var status = parado

if ( status = parado){
    function start(tarefa_pk) {
        cron = setInterval(() => { timer(); }, tempo);
        console.log('Execução da Tarefa ' + tarefa_pk + ' cadastrada!');
    
        $.ajax({                       // initialize an AJAX request
            url: 'http://localhost:8000/cadastrar_execucao',                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'tarefa_pk': tarefa_pk       // add the country id to the GET parameters
            },
            success: function (data) {
                console.log('Ajax: Execução da Tarefa ' + tarefa_pk + ' cadastrada!');
            }
        });   
    }
    status = execucao 
}    
function pause() {
    clearInterval(cron);
}
if ( status = execucao){
    function stop() {
        clearInterval(cron);
        hh = 0;
        mm = 0;
        ss = 0;

        document.getElementById('counter').innerText = '00:00:00';
    }
    status = parado
}

function timer() {
    ss++;

    if (ss == 59) { 
        ss = 0; 
        mm++; 

        if (mm == 59) { 
            mm = 0;
            hh++;
        }
    }
    var format = (hh < 10 ? '0' + hh : hh) + ':' + (mm < 10 ? '0' + mm : mm) + ':' + (ss < 10 ? '0' + ss : ss);
    
    
    document.getElementById('counter').innerText = format;

    return format;
}
