using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NUnit.Framework;

namespace AdventOfCode.Day_1
{
    [TestFixture]
    public class Day1Test
    {
        [Test]
        public void Test1()
        {
            Console.WriteLine(new Day1Solution().Part1());
        }

        [Test]
        public void Test2()
        {
            Console.WriteLine(new Day1Solution().Part2());
        }
    }
}
