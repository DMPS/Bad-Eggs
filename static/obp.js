var accountid = ["65468154-d0d4-4a4e-b743-89d794f2c0dd"];
function results(){
	console.log("function is called!");
	$.getJSON("https://apisandbox.openbankproject.com/obp/v1.2.1/banks/obp-bank-x-r/accounts/"+accountid[0]+"/public/transactions", 
               function( data ) {
		console.log(data.transactions);
        var names = data.transactions.map(function(tr) {
            return tr.other_account.holder.name;
        });
        names[10] = "AAB";
        console.log(names);
        var list = document.getElementById('transaction_list');
        names.forEach(function(name) {
            var li = document.createElement('li');
            li.appendChild(document.createTextNode(name));
            list.appendChild(li);
        });
	})
}

function opencorp(searchterm) {
    console.log(searchterm);
    $.get('/opencorp', { q: searchterm }, function(data) {
        console.log(data);
        var list = document.getElementById('results');
        data.result.forEach(function(c){
            var li = document.createElement('li');
            var text = "";
            text += c.name;
            if($.isEmptyObject(c.suspicious))
                text += ": Nothing suspicious";
            else {
                text += ": Something suspicious! ";
                if( 'inc_date' in c.suspicious )
                    text += "The company was never incorporated";
                if( 'dissolution_date' in c.suspicious )
                    text += "The company has been dissoved";
            }
            li.appendChild(document.createTextNode(text));
            list.appendChild(li);
        });
    });
}

function sanctions(searchterm) {
    $.getJSON('/sanctions', { q: searchterm }, function(data) {
        if('code' in data) {
            console.log('Cool');
            var elem = document.getElementById('sanctions');
            var p = document.createElement('p');
            var text = "";
            text += 'This company is not in the sanctions list!';
            p.className = "good";
            p.appendChild(document.createTextNode(text));
            elem.appendChild(p);
        }
        else {
            console.log(data);
            var elem = document.getElementById('sanctions');
            var p = document.createElement('p');
            var text = "";
            text += 'This company is in the sanctions list!   ';
            if( 'Other_Information' in data )
                text += data.Other_Information;
            p.className = "bad";
            p.appendChild(document.createTextNode(text));
            elem.appendChild(p);
        }
    });
}
