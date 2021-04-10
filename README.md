# Design Patterns

This repo contains code related to design patterns course.

## Introduction

- What are design patterns? : solution for common design problems

- Classification

    - Creational design patterns : Object creation
    - Structural design patterns : Object relationships
    - Behavioral design patterns : Object interaction and responsibilities

- SOLID

    - Single responsibility
    - Open - Closed
    - Liskov substitution
    - Interface segregation
    - Dependency inversion

Abstractions introduced in PEP 3119 in 2008 in Python 2.6 and 3.0.

## Strategy Pattern

Behavioral pattern
Functions and lambdas can be used to implement strategy pattern.
Encapsulates algorithms

## Observer Pattern

- Separation of concerns
- Single responsibility principle
- Interface segregation principle
- Open Close principle
- Dependency inversion principle
- Encapsulate what varies

## Command Pattern

- Single responsibility principle
- Open Closed principle
- Dependency inversion principle
- Long list of if/elif clauses

## Singleton Pattern

There are 5 different ways to implement Singleton in python

- Simple implementation
- Building base class with __new__ override
- Building metaclass
- Building MonoState base class
- Python module py_singleton

## Builder Pattern

Problems solved

- Separates how from what
- Encapsulates what varies
- Permits different representation

## Factory Pattern

- open closed
- dependencies
- separation concerns

## Null Pattern

- Provide default object with minimum implementation to avoid null checks

## Unit tests to check implementations

Run *python3 -m unittest* in each respective module folder
