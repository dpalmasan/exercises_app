INSERT INTO exercises (
  name,
  url,
  is_timed,
  duration,
  created_at,
  modified_at
)

VALUES
(
  'Jumping Jacks',
  'https://www.youtube.com/watch?v=iSSAk4XCsRA',
  1,
  30,
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
),
(
  'Incline Push Up',
  'https://www.youtube.com/watch?v=Z0bRiVhnO8Q',
  0,
  16,
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
),
(
  'Knee Push Ups',
  'https://www.youtube.com/watch?v=pUJnPMjYLxU',
  0,
  12,
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
),
(
  'Push Ups',
  'https://www.youtube.com/watch?v=IODxDxX7oi4',
  0,
  10,
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
),
(
  'Wide Grip Push Up',
  'https://www.youtube.com/watch?v=rr6eFNNDQdU',
  0,
  10,
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
),
(
  'Incline Push Up',
  'https://www.youtube.com/watch?v=Z0bRiVhnO8Q',
  0,
  12,
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
),
(
  'Box Push Up',
  'https://www.youtube.com/watch?v=3K8T3JSA2H8',
  0,
  12,
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
),
(
  'Wide Grip Push Up',
  'https://www.youtube.com/watch?v=rr6eFNNDQdU',
  0,
  10,
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
),
(
  'Hindu Push Up',
  'https://www.youtube.com/watch?v=nBLy1IGtSJ8',
  0,
  10,
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
),
(
  'Cobra Stretch',
  'https://www.youtube.com/watch?v=JDcdhTuycOI',
  1,
  20,
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
),
(
  'Doorway Chest Stretch',
  'https://www.youtube.com/watch?v=rT7rgXQtDcI',
  1,
  20,
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
);

INSERT INTO routines (
  title,
  description,
  created_at,
  modified_at
)

VALUES
(
  'Beginners Chest Workout',
  'A routine to train your chest. Beginners level.',
  '2019-03-03 18:23:00',
  '2019-03-03 18:23:00'
);

INSERT INTO association (
  routine_id,
  exercise_id
)

VALUES
(
  1, 1
),
(
  1, 2
),
(
  1, 3
),
(
  1, 4
),
(
  1, 5
),
(
  1, 6
),
(
  1, 7
),
(
  1, 8
),
(
  1, 9
),
(
  1, 10
),
(
  1, 11
);
