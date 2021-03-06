test = {
  'name': 'Loops',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> n = 3
          >>> while n >= 0:  # If this loops forever, just type Infinite Loop
          ...     n -= 1
          ...     print(n)
          2
          1
          0
          -1
          """,
        },
        {
          'code': """
          >>> n = 4
          >>> while n > 0:  # If this loops forever, just type Infinite Loop
          ...     n += 1
          ...     print(n)
          Infinite Loop
          """,
        },
        {
          'code': """
          >>> def go(n):
          ...     if n % 2 != 0:
          ...         print(n / 2)
          ...         return
          ...     while n > 0:
          ...         print(n)
          ...         n = n // 2
          >>> go(4)  # If this loops forever, just type Infinite Loop
          4
          2
          1
          >>> go(5)  # If this loops forever, just type Infinite Loop
          2.5
          """,
        }
      ]
    },
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> zero = 2
          >>> while zero != 0: # If this loops forever, just type Infinite Loop
          ...    zero = zero // 2
          ...    print(zero)
          1
          0
          """,
        },
        {
          'code': """
          >>> positive = 28
          >>> while positive: # If this loops forever, just type Infinite Loop
          ...    print("positive?")
          ...    positive -= 3
          Infinite Loop
          """,
        },
        {
          'code': """
          >>> positive = -9
          >>> negative = -12
          >>> while negative: # If this loops forever, just type Infinite Loop
          ...    if positive:
          ...        print(negative)
          ...    positive += 3
          ...    negative += 3
          -12
          -9
          -6
          """,
        },
      ]
    }
  ]
}
