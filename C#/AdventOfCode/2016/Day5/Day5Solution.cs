using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using NUnit.Framework;
using System.Text.RegularExpressions;
using System.Text;

namespace AdventOfCode
{
    public class Day5Solution : ISolution
    {
        public string Part1()
        {
            var input = "uqwqemis";

            var password = new StringBuilder();

            var i = 0;
            while(password.Length < 8)
            {
                var thisHash = CreateMD5(input + i);

                if (thisHash.StartsWith("00000"))
                {
                    password.Append(thisHash[5]);
                }

                i++;
            }

            return password.ToString();
        }

        public string Part2()
        {
            var input = "uqwqemis";

            var password = Enumerable.Repeat('x', 8).ToArray();

            var i = 0;
            while (password.Any(x => x.Equals('x')))
            {
                var thisHash = CreateMD5(input + i);

                if (thisHash.StartsWith("00000"))
                {
                    var thisPosition = int.Parse(thisHash[5].ToString(), System.Globalization.NumberStyles.HexNumber);

                    if(thisPosition < 8 && password[thisPosition].Equals('x'))
                        password[thisPosition] = thisHash[6];
                }

                i++;
            }

            return new string(password);
        }

        public string CreateMD5(string input)
        {
            // Use input string to calculate MD5 hash
            using (System.Security.Cryptography.MD5 md5 = System.Security.Cryptography.MD5.Create())
            {
                byte[] inputBytes = System.Text.Encoding.ASCII.GetBytes(input);
                byte[] hashBytes = md5.ComputeHash(inputBytes);

                // Convert the byte array to hexadecimal string
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < hashBytes.Length; i++)
                {
                    sb.Append(hashBytes[i].ToString("X2"));
                }
                return sb.ToString();
            }
        }
    }
}
