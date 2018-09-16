using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NUnit.Framework;

namespace AdventOfCode
{
    [TestFixture]
    public class TestFixture
    {
        private List<ISolution> _solutions;

        [OneTimeSetUp]
        public void Before()
        {
            _solutions = new List<ISolution>
            {
                new Day1Solution(),
                new Day2Solution()
            };
        }

        [Test]
        public void FullSuite()
        {
            for(var i=0; i<_solutions.Count; i++)
            {
                Console.WriteLine("Day {0} part {1} solution: {2}", i + 1, 1, _solutions[i].Part1());
                Console.WriteLine("Day {0} part {1} solution: {2}", i + 1, 2, _solutions[i].Part2());
                Console.Write(Environment.NewLine);
            }
        }
    }
}
