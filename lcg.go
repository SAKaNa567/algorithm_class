package main

import "fmt"

func rand1(n int) []int32{
  var x int32
  x = 53402397
  rand_seq := []int32{}
  for i:=0;i<n;i++{
    x = 65539 *x + 125654
    if x < 0{
      x += 2147483647
      x += 1
    }
    rand_seq = append(rand_seq,x)
  }
  return rand_seq
}

func rand2(n int) []int32{
  var x int32 = 1
  var A int32 = 48271
  var M int32 = 2147483647
  var Q int32 = M/A
  var R int32 = M%A
  rand_seq := []int32{}
  for i:=0;i<n;i++{
    x = A* (x%Q) - R*(x%Q)
    if x < 0{
        x = x + M
      }
    rand_seq = append(rand_seq,x)
    }
  return rand_seq

}

func rand3(n int)[]int32{
    var x int32 = 1
    var next int32 = 0
    A := rand2(55)
    rand_seq := []int32{}
    for i:=0 ;i<n;i++{
        j := (next + 31 ) % 55
        x = A[j] - A[next]
        if x < 0{
            x = x + 2147483647
            x = x + 1
        }
        A[next] = x
        next = (next + 1) % 55
        rand_seq = append(rand_seq,x)
      }
    return rand_seq
}


func main(){
  // answerlist := rand1(10)

  // for _,i :=  range answerlist{
  //   fmt.Println(float32(i)/2147483647)
  // }
  fmt.Println(rand1(5))
  fmt.Println(rand2(5))
  fmt.Println(rand3(5))


  return
}
