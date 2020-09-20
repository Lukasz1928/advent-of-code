using System;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;

namespace aoc {

    class MainClass {
        static void Main(string[] args) {
            MainClass mclass = new MainClass();
            int solution = mclass.solve();
            Console.WriteLine(solution);
        }

        private MD5 md5;

        public MainClass() {
            md5 = MD5.Create();
        }

        private String calculateHash(String key) {
            byte[] longKeyBytes = System.Text.Encoding.ASCII.GetBytes(key);
            byte[] hashBytes = md5.ComputeHash(longKeyBytes);
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < hashBytes.Length; i++) {
                sb.Append(hashBytes[i].ToString("X2"));
            }
            return sb.ToString();
        }

        public int solve() {
            String key = readInput();
            int num = 1;
            String hash;
            while(true) {
                hash = calculateHash(key + num.ToString());
                if(hash.StartsWith("000000")) {
                    break;
                }
                num++;
            }
            return num;
        }

        private String readInput() {
            return System.IO.File.ReadAllText("input");
        }
    }
}
