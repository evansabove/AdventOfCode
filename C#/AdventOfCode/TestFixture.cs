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
            var type = typeof(ISolution);
            var types = AppDomain.CurrentDomain.GetAssemblies()
                .SelectMany(s => s.GetTypes())
                .Where(p => type.IsAssignableFrom(p) && !p.IsInterface)
                .OrderBy(x => x.Name);

            _solutions = new List<ISolution>();

            foreach(var t in types)
            {
                _solutions.Add((ISolution)Activator.CreateInstance(t));
            }
        }

        [Test]
        public void FullSuite()
        {
            for (var i = 0; i < _solutions.Count; i++)
            {
                Console.WriteLine("Day {0} part {1} solution: {2}", i + 1, 1, _solutions[i].Part1());
                Console.WriteLine("Day {0} part {1} solution: {2}", i + 1, 2, _solutions[i].Part2());
                Console.Write(Environment.NewLine);
            }
        }

        [Test]
        public void Day4()
        {
            var day4 = new Day4Solution();
            Assert.True(day4.RoomIsDecoy("aaaaabbbzyx", "abxyz"));
            Assert.True(day4.RoomIsDecoy("abcdefgh", "abcde"));
            Assert.True(day4.RoomIsDecoy("notarealroom", "oarel"));
            Assert.False(day4.RoomIsDecoy("totallyrealroom", "decoy"));
        }

        [Test]
        public void Day4_2()
        {
            var day4 = new Day4Solution();
            Assert.AreEqual("cde", day4.Shift("abc", 2));
            Assert.AreEqual("zab", day4.Shift("xyz", 2));
        }

        [Test]
        public void Day5()
        {
            var day5 = new Day5Solution();
            Console.WriteLine(day5.Part2());
        }

        [Test]
        public void Day6()
        {
            var day6 = new Day6Solution();
            Console.WriteLine(day6.Part1());
            Console.WriteLine(day6.Part2());
        }

        [Test]
        public void Day7()
        {
            var day7 = new Day7Solution();

            Assert.True(day7.SupportsTls("abba[mnop]qrst"));
            Assert.False(day7.SupportsTls("abcd[bddb]xyyx"));
            Assert.False(day7.SupportsTls("aaaa[qwer]tyui"));
            Assert.True(day7.SupportsTls("ioxxoj[asdfgh]zxcvbn"));

            Console.WriteLine(day7.Part1());

            Assert.True(day7.SupportsSsl("aba[bab]xyz"));
            Assert.False(day7.SupportsSsl("xyx[xyx]xyx"));
            Assert.True(day7.SupportsSsl("aaa[kek]eke"));
            Assert.True(day7.SupportsSsl("zazbz[bzb]cdb"));

            Console.WriteLine(day7.Part2());
        }
    }
}
