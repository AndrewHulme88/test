class Person<T> {
  private Person<T> nextPerson;

  public Person<T> getNextPerson() {
      return nextPerson;
  }

  public void setNextPerson(Person<T> nextPerson) {
      this.nextPerson = nextPerson;
  }
}
