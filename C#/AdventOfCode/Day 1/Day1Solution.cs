using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using NUnit.Framework;
using System.Text.RegularExpressions;

namespace AdventOfCode
{
    public enum Direction
    {
        North = 0,
        East = 1,
        South = 2,
        West = 3
    }

    public class Day1Solution
    {
        private Direction _currentDirection = Direction.North;
        private int _currentX = 0;
        private int _currentY = 0;

        /*
         * You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

            The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

            There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

            For example:

            Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
            R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
            R5, L5, R5, R3 leaves you 12 blocks away.
            How many blocks away is Easter Bunny HQ?
         */
        public int Part1()
        {
            var input = File.ReadAllText(Path.Combine(TestContext.CurrentContext.TestDirectory, "Day 1", "input.txt"));
            
            var directions = input.Split(',').Select(x => x.Trim());

            foreach(var d in directions)
            {
                _currentDirection = GetNewDirection(d.First());
                var distance = int.Parse(Regex.Match(d, @"\d+").Value);

                switch(_currentDirection)
                {
                    case Direction.North:
                        _currentY += distance;
                        break;
                    case Direction.East:
                        _currentX += distance;
                        break;
                    case Direction.South:
                        _currentY -= distance;
                        break;
                    case Direction.West:
                        _currentX -= distance;
                        break;
                }
            }

            return Math.Abs(_currentX) + Math.Abs(_currentY);
        }

        /*
         * Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

            For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

            How many blocks away is the first location you visit twice?
         */
        public int Part2()
        {
            var input = File.ReadAllText(Path.Combine(TestContext.CurrentContext.TestDirectory, "Day 1", "input.txt"));

            var directions = input.Split(',').Select(x => x.Trim());

            var visitedLocations = new List<Tuple<int, int>>();

            foreach (var d in directions)
            {
                _currentDirection = GetNewDirection(d.First());
                var distance = int.Parse(Regex.Match(d, @"\d+").Value);

                switch (_currentDirection)
                {
                    case Direction.North:
                        for(var i=0; i<distance; i++)
                        {
                            if(visitedLocations.Any(x => x.Item1 == _currentX && x.Item2 == _currentY))
                                return Math.Abs(_currentX) + Math.Abs(_currentY);

                            visitedLocations.Add(new Tuple<int, int>(_currentX, _currentY));
                            _currentY++;
                        }

                        break;
                    case Direction.East:
                        for (var i=0; i<distance; i++)
                        {
                            if (visitedLocations.Any(x => x.Item1 == _currentX && x.Item2 == _currentY))
                                return Math.Abs(_currentX) + Math.Abs(_currentY);

                            visitedLocations.Add(new Tuple<int, int>(_currentX, _currentY));
                            _currentX++;
                        }

                        break;
                    case Direction.South:
                        for (var i=0; i<distance; i++)
                        {
                            if (visitedLocations.Any(x => x.Item1 == _currentX && x.Item2 == _currentY))
                                return Math.Abs(_currentX) + Math.Abs(_currentY);

                            visitedLocations.Add(new Tuple<int, int>(_currentX, _currentY));
                            _currentY--;
                        }

                        break;
                    case Direction.West:
                        for (var i = 0; i < distance; i++)
                        {
                            if (visitedLocations.Any(x => x.Item1 == _currentX && x.Item2 == _currentY))
                                return Math.Abs(_currentX) + Math.Abs(_currentY);

                            visitedLocations.Add(new Tuple<int, int>(_currentX, _currentY));
                            _currentX--;
                        }
                        break;
                }
            }

            return Math.Abs(_currentX) + Math.Abs(_currentY);
        }

        private Direction GetNewDirection(char letter)
        {
            switch (_currentDirection)
            {
                case Direction.North:
                    return letter == 'L' ? Direction.West : Direction.East;
                case Direction.East:
                    return letter == 'L' ? Direction.North : Direction.South;
                case Direction.South:
                    return letter == 'L' ? Direction.East : Direction.West;
                case Direction.West:
                    return letter == 'L' ? Direction.South : Direction.North;
            }

            return 0;
        }
    }

}
