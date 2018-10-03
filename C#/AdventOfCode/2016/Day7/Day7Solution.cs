using System.Text.RegularExpressions;

using NUnit.Framework;
using System.IO;
using System.Linq;

namespace AdventOfCode
{
    // With a little inspiration from the solutions of https://github.com/mattsharpe 
    public class Day7Solution : ISolution
    {
        private Regex _abbaInsideHyperNet = new Regex(@"(\w)(\w)\2\1\w*(?=\])");
        private Regex _abba = new Regex(@"(\w)(\w)\2\1(?!\])");

        public string Part1()
        {
            var input = File.ReadAllLines(Path.Combine(TestContext.CurrentContext.TestDirectory, "2016", "Day7", "input.txt"));

            return input.Where(SupportsTls).Count().ToString();
        }

        public bool SupportsTls(string input)
        {
            if (_abbaInsideHyperNet.IsMatch(input))
                return false;

            var abbaMatches = _abba.Matches(input);
            if (abbaMatches.Count == 0)
                return false;

            //return false if all letters are the same
            return abbaMatches[0].Value.GroupBy(x => x).Count() != 1;
        }

        public string Part2()
        {
            var input = File.ReadAllLines(Path.Combine(TestContext.CurrentContext.TestDirectory, "2016", "Day7", "input.txt"));

            return input.Where(SupportsTls).Count().ToString();
        }

        public bool SupportsSsl(string input)
        {
            // Would rather get this all in one regex, but y'know...tis a learning curve
            var supernetPart1 = new Regex(@"(?<=^)(\w)(\w)\1");
            var supernetPart2 = new Regex(@"(\w)(\w)\1(?=$)");

            var matches1 = supernetPart1.IsMatch(input);
            var matches2 = supernetPart2.IsMatch(input);

            //get match, change the order and then match it 

            var hypertextString = "";

            if(matches1)
            {
                var matches = supernetPart1.Matches(input);
                var match = matches[0];

                hypertextString = string.Join("", match.Value[1], match.Value[0], match.Value[1]);

                var hypernet = new Regex(@"\[" + hypertextString + "\\]");
                if (hypernet.IsMatch(input))
                    return true;
            }

            if(matches2)
            {
                var match = supernetPart2.Match(input);
                hypertextString = string.Join("", match.Value[1], match.Value[0], match.Value[1]);

                var hypernet = new Regex(@"\[" + hypertextString + "\\]");
                if (hypernet.IsMatch(input))
                    return true;
            }

            return false;
        }
    }
}
