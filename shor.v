import math

fn find_r(n int, base_number int) int {
  mut rest := 1
  mut nb := n
  mut index := 1

  for {
    rest = int(math.mod(nb * rest, base_number))
    if rest == 1 {
      return index
    }
    index += 1
  }
  return index
}

fn find_gcd(a int, b int) int {
  if b == 0 { return a }
  mut aa := a
  mut bb := b
  mut temp := 0
  for bb != 0 {
    temp = int(math.mod(aa, bb))
    aa = bb
    bb = temp
  }
  return aa 
}

fn main() {
  number := 27221
  mut r := 1
  mut rd := 2

  for r % 2 != 0 || find_gcd(rd, number) != 1 {
    rd += 1
    r = find_r(rd, number)
  }
  
  mut rest := 1
  for _ in 0..int(r/2) {
    rest = int(math.mod(rd * rest, number))
  }

  fac1 := find_gcd(number, rest-1)
  fac2 := find_gcd(number, rest+1)
  println(fac1)
  println(fac2)
}
