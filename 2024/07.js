inp = `A:+,-,=,=
B:+,=,-,+
C:=,-,+,+
D:=,=,=,+`;
rt = `S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-`;

ft = "";
rt = rt.split("\n");
seen = new Set();
var [x, y] = [0, 0];
for (i = 0; i < 1000; i++) {
  for ([dx, dy] of [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ]) {
    [nx, ny] = [x + dx, y + dy];
    if (
      nx >= rt[0].length ||
      nx < 0 ||
      ny >= rt.length ||
      ny < 0 ||
      seen.has(`${nx},${ny}`) ||
      rt[ny][nx] == " " ||
      rt[ny][nx] == undefined
    )
      continue;
    [x, y] = [nx, ny];
    break;
  }
  ft += rt[y][x];
  console.log([x, y]);
  if (rt[y][x] == "S") break;
  seen.add(`${x},${y}`);
}

console.log(ft);

plans = inp
  .split("\n")
  .map((l) => l.split(":"))
  .map((l) => [l[0], l[1].split(",")]);

plan_essence = {};
essence_total = {};
for (p of plans) {
  plan_essence[p[0]] = 10;
  essence_total[p[0]] = 0;
}

rounds = 10 * ft.length;
for (i = 0; i < rounds; i++) {
  for (p of plans) {
    plan_essence[p[0]] += "S=".includes(ft[i % ft.length])
      ? { "+": 1, "-": -1, "=": 0 }[p[1][i % p[1].length]]
      : { "+": 1, "-": -1, "=": 0 }[ft[i % ft.length]];
    essence_total[p[0]] += plan_essence[p[0]];
  }
}

essence_total = Object.entries(essence_total);
// essence_total.sort((a,b)=>a[1]<b[1])//.map(a=>a[0]).join('')

function conv(i) {
  s = "";
  for (j = 0; j < 11; j++) s = "+-="[Math.floor(i / 3 ** j) % 3] + s;
  return s;
}

// console.log(Array(1000).entries().map((i,j)=>conv(j)).toArray())

// allPlans=getCombinations('+++++---==='.split('')).filter(p=>p.length==11)
// // for (p of getCombinations('+++++---==='.split('')))console.log
// console.log(allPlans)
function count(l, i) {
  return l.split("").filter((t) => t == i).length;
}
lps = [];
for (i = 0; i < 3 ** 11; i++) {
  p = conv(i);
  if (count(p, "+") == 5 && count(p, "-") == 3 && count(p, "=") == 3)
    lps.push(p);
}

for (p of lps) {
  pe = 10;
  et = 0;
  for (i = 0; i < rounds; i++) {
    for (p of plans) {
      pe += "S=".includes(ft[i % ft.length])
        ? { "+": 1, "-": -1, "=": 0 }[p[1][i % p[1].length]]
        : { "+": 1, "-": -1, "=": 0 }[ft[i % ft.length]];
      et += pe;
    }
  }
}
