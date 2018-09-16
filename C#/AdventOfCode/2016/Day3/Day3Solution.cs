using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using NUnit.Framework;

namespace AdventOfCode
{
    public class Day3Solution : ISolution
    {
        public string Part1()
        {
            var input = File.ReadAllLines(Path.Combine(TestContext.CurrentContext.TestDirectory, "2016", "Day3", "input.txt"));

            var validTriangles = 0;

            foreach(var line in input)
            {
                var lengths = line.Split(' ')
                    .Where(x => x != string.Empty)
                    .Select(x => int.Parse(x))
                    .OrderBy(x => x).ToList();

                if(lengths[0] + lengths[1] > lengths[2])
                {
                    validTriangles++;
                }
            }

            return validTriangles.ToString();
        }

        public string Part2()
        {
            var input = File.ReadAllLines(Path.Combine(TestContext.CurrentContext.TestDirectory, "2016", "Day3", "input.txt"));

            var validTriangles = 0;

            var rowGroups = new List<Tuple<int, int, int>>();

            foreach (var line in input)
            {
                var lengths = line.Split(' ')
                    .Where(x => x != string.Empty)
                    .Select(x => int.Parse(x))
                    .ToList();

                rowGroups.Add(new Tuple<int, int, int>(lengths[0], lengths[1], lengths[2]));
            }

            var newList = rowGroups.Select(x => x.Item1).ToList();
            newList.AddRange(rowGroups.Select(x => x.Item2));
            newList.AddRange(rowGroups.Select(x => x.Item3));

            for(var i=0; i<newList.Count/3; i++)
            {
                var lengths = newList
                    .Skip(i * 3)
                    .Take(3)
                    .OrderBy(x => x)
                    .ToList() ;

                if (lengths[0] + lengths[1] > lengths[2])
                {
                    validTriangles++;
                }
            }

            return validTriangles.ToString();
        }
    }
}
