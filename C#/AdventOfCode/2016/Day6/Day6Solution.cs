using NUnit.Framework;
using System.IO;
using System.Linq;
using System.Text;

namespace AdventOfCode
{
    public class Day6Solution : ISolution
    {
        public string Part1()
        {
            var input = File.ReadAllLines(Path.Combine(TestContext.CurrentContext.TestDirectory, "2016", "Day6", "input.txt"));

            var finalString = new char[input.First().Length];

            for(int i=0; i<input.First().Length; i++)
            {
                finalString[i] = input.Select(x => x[i])
                    .GroupBy(x => x)
                    .OrderByDescending(x => x.Count())
                    .First().Key;
            }

            return new string(finalString);
        }

        public string Part2()
        {
            var input = File.ReadAllLines(Path.Combine(TestContext.CurrentContext.TestDirectory, "2016", "Day6", "input.txt"));

            var finalString = new char[input.First().Length];

            for (int i = 0; i < input.First().Length; i++)
            {
                finalString[i] = input.Select(x => x[i])
                    .GroupBy(x => x)
                    .OrderBy(x => x.Count())
                    .First().Key;
            }

            return new string(finalString);
        }
    }
}
