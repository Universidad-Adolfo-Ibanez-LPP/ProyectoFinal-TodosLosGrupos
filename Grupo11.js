const cheerio = require('cheerio');
const axios = require('axios');
const fetch = require('node-fetch');
let fs = require('fs');

const _private = new WeakMap();  // para más adelante setear las propiedades de las clases y dejarlas como privadas

function crearCsv(fileName,stats) {
    fs.writeFile(fileName, stats.toString(), function (err) {  // escibimos archivo
            if (err) {console.log(err);}
        }
    )
}

/* class Farmacia {
    constructor(nombreFarmacia) {
        const propiedades = {
            _NombreFarmacia: nombreFarmacia
        }
        _private.set(this, {propiedades});  // para setear todas las propiedades como privadas
    }
    get nombreFarmacia() { return _private.get(this).propiedades['_NombreFarmacia']; }
    set nombreFarmacia(nuevoNombre) { return _private.get(this).propiedades['_NombreFarmacia'] = nuevoNombre; }
}
*/


class Medicamento {  // clase medicamento hereda las propiedades de Farmacia

    // CONSTRUCTORES
    constructor(nombre, farmacia, precioCLP, precioUF , descripcion, principio_activo) {  // constructor de la clase medicamento
        // super(farmacia);  // le pasamos el atributo del nombre de la farmacia al padre de Medicamento, es decir a Farmacia
        const propiedades = {  // creamos un objeto que tendrá las propiedades de un medicamento
            _Nombre: nombre,
            _Farmacia: farmacia,
            _PrecioCLP: precioCLP,
            _PrecioUF: precioUF,
            _Descripcion: descripcion,
            _Principio: principio_activo
        }
        _private.set(this, {propiedades});  // para setear todas las propiedades como privadas (encapsulamiento)
    }

    // MÉTODOS DE ACCESO
    // Getters
    get nombre() { return _private.get(this).propiedades['_Nombre']; }
    get farmacia() { return _private.get(this).propiedades['_Farmacia']; }
    get precioCLP() { return _private.get(this).propiedades['_PrecioCLP']; }
    get precioUF() { return _private.get(this).propiedades['_PrecioUF']; }
    get descripcion() { return _private.get(this).propiedades['_Descripcion']; }
    get principio_activo() { return _private.get(this).propiedades['_Principio']; }
    // Setters
    set nombre(nuevoNombre) { return _private.get(this).propiedades['_Nombre'] = nuevoNombre; }
    set farmacia(nuevaFarmacia) { return _private.get(this).propiedades['_Farmacia'] = nuevaFarmacia; }
    set precioCLP(nuevoPrecioCLP) { return _private.get(this).propiedades['_PrecioCLP'] = nuevoPrecioCLP; }
    set precioUF(nuevoPrecioUF) { return _private.get(this).propiedades['_PrecioUF'] = nuevoPrecioUF; }
    set descripcion(nuevaDescripcion) { return _private.get(this).propiedades['_Descripcion'] = nuevaDescripcion; }
    set principio_activo(nuevoPrincipio) { return _private.get(this).propiedades['_Principio'] = nuevoPrincipio; }
}

async function getUFValue(fileName) {  // devuelve un archivo .txt con la fecha actual y el precio de la uf actual
    let response = await fetch('https://www.bcentral.cl/web/banco-central'),
        html = await response.text();
    let $ = cheerio.load(html);  // traemos el texto de la página del banco central
    let precioUf = $('div[id = "_BcentralIndicadoresViewer_INSTANCE_pLcePZ0Eybi8_myTooltipDelegate"]')  // buscamos la información que está en la división de ese id
        .find('div > div > div > div > div > div > p').text().split('$')[1].split('U')[0];  // p que está en div que está en div... quiero el texto y el texto lo separo por comas

    // console.log($('h2').text());
    let uf = precioUf.replace(".", "");  // quitamos el punto del número
    global.ufNumero = Number.parseFloat(uf);
    let fechaHoy = new Date(Date.now());
    fechaHoy = fechaHoy.toDateString()  // conseguimos la fecha actual

    let fechaUf = fechaHoy.concat(';', uf)  // concatenamos la fecha actual con el precio de la uf actual

    fs.writeFile(fileName, fechaUf, function (err) {  // escibimos archivo
            if (err) {console.log(err);}
        }
    )
}

function getPrincipios(fileName) {  // entrega un arreglo con los principios que están en el archivo .txt entrgado
    let principios;
    try {
        principios = fs.readFileSync(fileName, 'utf8');
    } catch (err) {
        console.error(err);
    }
    principios = principios.split("\r\n");
    return principios;
}

let sinTildes = (function() {  // función que elimina todos los tildes de una cadena de texto. // sacado en https://es.stackoverflow.com/questions/62031/eliminar-signos-diacr%C3%ADticos-en-javascript-eliminar-tildes-acentos-ortográficos
    let de = 'ÁÃÀÄÂÉËÈÊÍÏÌÎÓÖÒÔÚÜÙÛÑÇáãàäâéëèêíïìîóöòôúüùûñç',
        a = 'AAAAAEEEEIIIIOOOOUUUUNCaaaaaeeeeiiiioooouuuunc',
        re = new RegExp('['+de+']' , 'ug');
    return texto =>
        texto.replace(
            re,
            match => a.charAt(de.indexOf(match))
        );
})();

function arraySinTildes(array) {
    return array.map(function (elemento){
        return sinTildes(elemento);
    });
}

let arrayfinal=[]
let cont = 4
async function getFarmaciasInfo(links) {

    if (JSON.stringify(links) === JSON.stringify([])) {
        promedio_Total= promedioTOTAL(arrayfinal, principios[0]);
        promedio_Principio= PromediosPrincipios(arrayfinal)
        promedio_Farmacia=promedioporfarmacia(arrayfinal,principios[0],"Farmacia Ahumada")
        Menor_precio=MenorPrecio(arrayfinal,principios[0])

        crearCsv('./promedio_Total',promedio_Total)
        crearCsv('./promedio_Farmacia',promedio_Farmacia)
        crearCsv('./Menor_precio',Menor_precio)
        crearCsv('./info',arrayfinal)
        crearCsv('./promedio_Principio',promedio_Principio)



        return arrayfinal;
    }

    let linksUnPrincipio = links.pop();  // consigo los dos links para un mismo principio

    let linkAhumada = linksUnPrincipio[0][0];
    let linkDrsimi = linksUnPrincipio[0][1];

    let responseAhumada = await fetch(linkAhumada),
        htmlAhumada = await responseAhumada.text();  // traemos el texto de la página
    let $A = cheerio.load(htmlAhumada);

    let responseDrsimi = await fetch(linkDrsimi),
        htmlDrsimi = await responseDrsimi.text();  // traemos el texto de la página
    let $S = cheerio.load(htmlDrsimi);

    getAhumadaInfo($A,cont);
    getDrsimiInfo($S, cont);

    arrayfinal.push(arraymedicamentosAhumada)
    arrayfinal.push(arraymedicamentosDrSimi)
    getFarmaciasInfo(links);
    cont -= 1

}

function getArrayofLinks(filename) {
    global.principios = getPrincipios(filename);
    principios = arraySinTildes(principios);

    return principios.map(function (principio) {
        principio = principio.replace(" ", "+");

        let links = [[]];
        let linksAhumada = `https://www.farmaciasahumada.cl/catalogsearch/result/?q=${principio}`;
        let linksDrsimi = `https://www.drsimi.cl/catalogsearch/result/?q=${principio}`;
        links[0].push(linksAhumada);
        links[0].push(linksDrsimi);

        return links;
    });
}

async function getAhumadaInfo($,cont) {

    let arraymedicamentos = []
    $("li[class='item product product-item']").each((i,elem) => {  // 'elem' es el elememnto que está recorriendo
        const nombre = $(elem).find('div[class="product details product-item-details"]').find('p[class="product-brand-name truncate"]').text();
        const precio = $(elem).find('div[class="product details product-item-details"]').find('div[class="priceSearchContainer "]').find('span[class="price"]').text();
        let precioCLP = Number.parseInt(precio.slice(1).replace(".",""));
        const precioUF = precioCLP/ufNumero;
        const descripcion = $(elem).find('div[class="product details product-item-details"]').find('strong[class="product name product-item-name truncate"]').find('a[class="product-item-link"]').text().trim();
        const principios = getPrincipios("princios_activos.txt")
        const principioactivo= principios[cont]
        let medicamento1 = new Medicamento(nombre, "Farmacia Ahumada", precioCLP , precioUF, descripcion, principioactivo)

        // console.log(medicamento1.principio_activo);

        arraymedicamentos.push(medicamento1);
        global.arraymedicamentosAhumada = arraymedicamentos;
    })
}

async function getDrsimiInfo($) {

    let arraymedicamentos = []
    $("ol[class='filterproducts products list items product-items ']").find("div[class='product-item-info type1']").each((i,elem) => {  // 'elem' es el elememnto que está recorriendo
        let nombre_descripcion = $(elem).find('div[class="product details product-item-details"]').find('a[class="product-item-link"]').text().trim();

        let split = nombre_descripcion.split(" ");  // separamos lo conseguido para obtener el nombre y la descripción del medicamento
        let nombre = split[0];
        let descripcion = split.join(" ");

        const precio = $(elem).find('div[class="price-box price-final_price"]').find('span[class="price-container price-final_price tax weee"]').find('span[class="price-wrapper "]').text();
        let precioCLP = Number.parseInt(precio.slice(1).replace(".",""));
        const precioUF = precioCLP/ufNumero;
        // const descripcion = $(elem).find('div[class="product details product-item-details"]').find('strong[class="product name product-item-name truncate"]').find('a[class="product-item-link"]').text();
        const principios = getPrincipios("princios_activos.txt")
        const principioactivo= principios[cont]
        let medicamento1 = new Medicamento(nombre, "Farmacia Dr Simi", precioCLP , precioUF, descripcion, principioactivo)

        // console.log(medicamento1.nombre, medicamento1.descripcion, medicamento1.farmacia, medicamento1.precioCLP, medicamento1.precioUF, medicamento1.descripcion, medicamento1.principio_activo);

        arraymedicamentos.push(medicamento1);
        global.arraymedicamentosDrSimi = arraymedicamentos;
    });
}

function promedioTOTAL(arr,principio) { //entrega el promedio de los principios
    let promedio;
    let suma = 0;
    let cont = 0;
    arr.map(Principio => {
        Principio.map(Medicamento => {
            if (Medicamento.principio_activo === principio && !isNaN(Medicamento.precioCLP)) {
                cont += 1;
                suma += Medicamento.precioCLP;
                promedio = suma / cont;
            }
        });
    });
    return promedio;
}

function promedioporfarmacia(arr,principio,farmacia){ //esta entrega los preciosxprincipioxfarmacia
    let promedio;
    let suma=0;
    let cont=0;
    arr.forEach(function (Principio){
        Principio.forEach(function (Medicamento){
            if(Medicamento.principio_activo === principio && Medicamento.farmacia === farmacia && !isNaN(Medicamento.precioCLP)){
                cont +=1;
                suma += Medicamento.precioCLP;
                promedio = suma/cont;
            }
        });
    });
    return promedio;
}


function MenorPrecio(arr,principio){ //entrega el menor precio en farmacia x por principio
    let nombre;
    let menor=100000000;
    let actual;
    let farmacia;
    let response;
    arr.forEach(function (Principio){
        Principio.forEach(function (Medicamento){
            actual=Medicamento.precioCLP;
            if(actual<= menor && Medicamento.principio_activo===principio && !isNaN(Medicamento.precioCLP)){
                nombre = Medicamento.nombre;
                menor = actual;
                farmacia = Medicamento.farmacia;
                response = [nombre,farmacia,menor];
            }
        });
    });
    return response
}

function info(arrayGeneral) {
    arrayGeneral.forEach(function (array){
        array.forEach(function (medicamento) {
            console.log(medicamento.nombre, medicamento.descripcion, medicamento.farmacia, medicamento.precioCLP, medicamento.precioUF, medicamento.descripcion, medicamento.principio_activo);
        });
    });
}


getUFValue('./parametros.txt');

let links = getArrayofLinks('princios_activos.txt')  // links que necesito investigar en la posición (0, 0) y (0, 1) están los links de ahumada y salcobrand para el primer principio y así sucesivamente

getFarmaciasInfo(links).then(val => console.log(val))



function PromediosPrincipios(arr){
    let promedios=[]
    let promedio1, promedio2, promedio3, promedio4, promedio5
    let suma1=0,sum2=0,suma3=0,suma4=0,suma5=0
    let cont1=0,cont2=0,cont3=0,cont4=0,cont5=0
    arr.forEach(function (Principio){
        Principio.forEach(function (Medicamento){
            if(Medicamento.principio_activo==='paracetamol'&& !isNaN(Medicamento.precioCLP)){
                cont1+=1
                suma1+=Medicamento.precioCLP
                promedio1= suma1/cont1
            }
            if(Medicamento.principio_activo==='ácido acetilsalicílico'&& !isNaN(Medicamento.precioCLP)){
                cont2+=1
                sum2+=Medicamento.precioCLP
                promedio2= sum2/cont2
            }
            if(Medicamento.principio_activo==='losartán'&& !isNaN(Medicamento.precioCLP)){
                cont3+=1
                suma3+=Medicamento.precioCLP
                promedio3= suma3/cont3
            }
            if(Medicamento.principio_activo==='metformina'&& !isNaN(Medicamento.precioCLP)){
                cont4+=1
                suma4+=Medicamento.precioCLP
                promedio4= suma4/cont4
            }
            if(Medicamento.principio_activo==='atorvastatina'&& !isNaN(Medicamento.precioCLP)){
                cont5+=1
                suma5+=Medicamento.precioCLP
                promedio5= suma5/cont5
            }
        })
    })
    promedios.push(promedio1,promedio2,promedio3,promedio4,promedio5)
    return promedios
}
