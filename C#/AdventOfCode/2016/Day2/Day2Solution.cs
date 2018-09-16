using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using NUnit.Framework;
using System.Text;

namespace AdventOfCode
{
    public class Day2Solution : ISolution
    {
        public string Part1()
        {
            var input = File.ReadAllLines(Path.Combine(TestContext.CurrentContext.TestDirectory, "2016", "Day2", "input.txt"));

            var keypad = new int[,]
            {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
            };

            var currentX = 1;
            var currentY = 2;

            var result = new StringBuilder();

            foreach (var instruction in input)
            {
                foreach (var step in instruction)
                {
                    switch (step)
                    {
                        case 'U':
                            currentX = Math.Max(0, currentX - 1);
                            break;
                        case 'D':
                            currentX = Math.Min(2, currentX + 1);
                            break;
                        case 'L':
                            currentY = Math.Max(0, currentY - 1);
                            break;
                        case 'R':
                            currentY = Math.Min(2, currentY + 1);
                            break;
                    }
                }

                result.Append(keypad[currentX, currentY]);
            }

            return result.ToString();
        }

        public string Part2()
        {
            var input = File.ReadAllLines(Path.Combine(TestContext.CurrentContext.TestDirectory, "2016", "Day2", "input.txt"));

            var keypad = new string[,]
            {
                {"x", "x", "1", "x", "x"},
                {"x", "2", "3", "4", "x"},
                {"5", "6", "7", "8", "9"},
                {"x", "A", "B", "C", "x"},
                {"x", "x", "D", "x", "x"},
            };

            var currentX = 0;
            var currentY = 2;

            var result = new StringBuilder();

            foreach (var instruction in input)
            {
                foreach (var step in instruction)
                {
                    switch (step)
                    {
                        case 'U':
                            currentX = Math.Max(0, currentX - 1);
                            if (keypad[currentX, currentY].Equals("x"))
                                currentX += 1;
                            break;
                        case 'D':
                            currentX = Math.Min(4, currentX + 1);
                            if (keypad[currentX, currentY].Equals("x"))
                                currentX -= 1;
                            break;
                        case 'L':
                            currentY = Math.Max(0, currentY - 1);
                            if (keypad[currentX, currentY].Equals("x"))
                                currentY += 1;
                            break;
                        case 'R':
                            currentY = Math.Min(4, currentY + 1);
                            if (keypad[currentX, currentY].Equals("x"))
                                currentY -= 1;
                            break;
                    }
                }

                result.Append(keypad[currentX, currentY]);
            }

            return result.ToString();
        }
    }
}
