export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  cloneCar() {
    const clonedCar = Object.create(Object.getPrototypeOf(this));
    Object.assign(clonedCar, this);
    return clonedCar;
  }
}

Object.defineProperty(Car, Symbol.species, {
  value: Car,
  writable: false,
});
