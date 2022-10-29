const greats = {
    'firstName' :'Carlos',
    'lastName' : 'Ruiz',
    'age' : 23,
    'country' : 'Nicaragua'
}

const sayHello = () =>{
    return `Hola mi nombre es ${greats.firstName} ${greats.lastName} y tengo ${greats.age} años y soy de ${greats.country}`
}

console.log('====================================');
console.log(sayHello());
console.log('====================================');