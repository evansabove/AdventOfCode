using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using NUnit.Framework;
using System.Text.RegularExpressions;
using System.Text;

namespace AdventOfCode
{
    public class Day4Solution : ISolution
    {
        public string Part1()
        {
            var input = File.ReadAllLines(Path.Combine(TestContext.CurrentContext.TestDirectory, "2016", "Day4", "input.txt"));

            var sectorIdSum = 0;

            foreach(var line in input)
            {
                var checkSum = line.Split('[', ']')[1];
                var dashTokens = line.Split('-').ToList();
                var encryptedName = string.Join("", dashTokens.Take(dashTokens.Count - 1));
                var sectorId = int.Parse(Regex.Match(line, @"\d+").Value);

                if (RoomIsDecoy(encryptedName, checkSum))
                    sectorIdSum += sectorId;
            }

            return sectorIdSum.ToString();
        }

        public bool RoomIsDecoy(string encryptedName, string checksum)
        {
            var letters = encryptedName.GroupBy(x => x)
                .OrderByDescending(g => g.Count())
                .ThenBy(g => g.Key)
                .Select(g => g.Key)
                .Take(5)
                .ToArray();

            return checksum.Equals(new string(letters));
        }

        public string Part2()
        {
            var input = File.ReadAllLines(Path.Combine(TestContext.CurrentContext.TestDirectory, "2016", "Day4", "input.txt"));

            foreach (var line in input)
            {
                var checkSum = line.Split('[', ']')[1];
                var dashTokens = line.Split('-').ToList();
                var encryptedName = string.Join(" ", dashTokens.Take(dashTokens.Count - 1));
                var sectorId = int.Parse(Regex.Match(line, @"\d+").Value);

                var decrypted = Shift(encryptedName, sectorId);
                //Console.WriteLine(decrypted + " - " + sectorId);

                if (decrypted.Equals("northpole object storage"))
                    return sectorId.ToString();
            }

            return null;
        }

        public string Shift(string s, int times)
        {
            var newString = new StringBuilder();

            foreach(var ch in s)
            {
                if (ch == ' ')
                {
                    newString.Append(ch);
                    continue;
                }

                var newChar = (char)(ch + times);
                
                while(newChar > 'z')
                {
                    newChar = (char)(newChar - 26);
                }

                newString.Append(newChar);
            }

            return newString.ToString();
        }
    }
}
