interface Person {
    first: string;
    last: string;
    [key: string]: any // allows more keys
}

const person: Person = {
    first: 'John',
    last: 'Doe'
}

const person2: Person = {
    first: 'idk',
    last: 'lol',
    middle: 'hi',
}

//strong type functions
function pow(x:number, y: number): void{
    Math.pow(x, y).toString();
}

//array
type MyList = [number?, string?, boolean?]
const arr: MyList = []
arr.push(1)
arr.push('23')
arr.push(false)

//generics
class Observable<T>{
    constructor(public value: T) {}
}
let x: Observable<number>;
let y: Observable<Person>;
let z = new Observable(23)