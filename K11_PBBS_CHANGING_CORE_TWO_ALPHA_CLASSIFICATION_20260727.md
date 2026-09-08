# No changing-core two-alpha portal at \(k=11\)

Date: 2026-07-27

Method: Boolean-octahedron overlap geometry and exact cyclic-parenthesis
endpoint tables; no computational search.

## 0. Result

Let

\[
Z=\{1,3,5,7,9\}
\]

be a lower row on the alternating component of the complemented centered
PBBS factor. There is no simple signed sum of two alpha vectors with
different rank-four cores such that

- the surviving negative side consists entirely of present PBBS diamonds;
- the alternating chord at \(Z\) survives on that negative side; and
- the sum changes the attachment of the alternating route.

Together with the fixed-core \(K_4\) audit, this proves that every alpha
commutator portal from the initial alternating component uses at least three
formal alphas.

## 1. Overlap geometry of two Boolean octahedra

An alpha with core \(R\), triangle roots \(i,j,k\), and spare \(\ell\) has
three lower rows

\[
R+i,\qquad R+j,\qquad R+k.
\]

It contains exactly one positive and one negative diamond at each of these
rows.

### Lemma 1.1

If two alphas share diamonds on two distinct lower rows, then their
rank-four cores are equal.

#### Proof

If \(Y_1\ne Y_2\) are two lower rows of one alpha, then

\[
Y_1\cap Y_2=R.
\]

The same identity recovers the core of the second alpha from the same two
rows. Hence the cores coincide. \(\square\)

Now let \(A\) be the alpha containing the surviving alternating negative
diamond. Since no executable alpha chart contains that chord, at least one
other negative diamond of \(A\) is absent from PBBS and must be cancelled by
a positive diamond of the second alpha \(B\).

If two negative diamonds of \(A\) were absent, the two cancellations would
occur on distinct lower rows, and Lemma 1.1 would force the cores to agree.
Thus a changing-core pair can use only an \(A\) with exactly one missing
negative diamond.

Let that missing diamond be \(d\), on lower row \(Y\). Any unavailable
negative diamond of \(B\) on a row other than \(Y\) would require a second
cross-cancellation on a distinct lower row, again forcing equal cores.
Therefore the two different-core possibilities are exhaustive:

1. **single cancellation:** \(B\) inserts \(d\), while its negative diamond
   at \(Y\) is the current PBBS chord and its other two negatives are present;
2. **double cancellation at one row:** \(B\) inserts \(d\) and its negative
   diamond at \(Y\) is the opposite diamond of \(A\), so both entries at
   \(Y\) cancel; its other two negatives are present.

Thus the global two-alpha problem reduces to two endpoint tests at one row.

## 2. The complete one-missing list through \(Z\)

Put \(R_x=Z\setminus\{x\}\).

### Forward family

For \(x\in\{3,5,7,9\}\), the unique spare-\(0\) alpha side with two present
negative diamonds has triangle roots

\[
\{x,10,x-1\}.
\]

Its negative diamonds are

\[
\begin{array}{c|c}
\text{lower row}&\text{endpoint pair}\\ \hline
R_x+x=Z&\{0,10\}\\
R_x+(x-1)&\{0,x\}\\
R_x+10&\{0,x-1\}.
\end{array}
\tag{2.1}
\]

The first two are present and the third is absent. Write

\[
Y_x=R_x+10,
\qquad
d_x=(Y_x,\{0,x-1\}).
\tag{2.2}
\]

The current PBBS chord at \(Y_x\) is

\[
\epsilon(Y_x)=
\begin{cases}
\{x-1,x+1\},&x=3,5,7,\\
\{8,9\},&x=9.
\end{cases}
\tag{2.3}
\]

At \(x=1\), the boundary nearly-alpha has negative diamonds

\[
Z:\{0,10\},\qquad
R_1+10:\{0,2\},\qquad
R_1+2:\{0,1\},
\tag{2.4}
\]

with only the last one absent.

### Reverse family

Reflection \(u\mapsto10-u\) gives the complete spare-\(10\) family. Hence it
is enough to exclude the forward cases.

The uniqueness in (2.1) follows directly from the exact clean-label sets
for \(R_x\): once the alternating pair fixes spare \(0\) and partner \(10\),
the only third root whose required pair \(\{0,x\}\) is present is \(x-1\).
The boundary \(x=1\) is (2.4).

## 3. Single-cancellation completion is impossible

Fix \(x\in\{3,5,7,9\}\). Suppose a different-core alpha \(B\) has \(d_x\)
on its positive side and deletes the current chord (2.3) at \(Y_x\).
Write its core as

\[
S=Y_x\setminus\{y\},
\qquad y\in R_x.
\]

The common endpoint of \(d_x\) and the current chord is \(x-1\). Thus the
spare of \(B\) is forced to be \(x-1\). Put

\[
v_x=
\begin{cases}
x+1,&x=3,5,7,\\
9,&x=9.
\end{cases}
\]

The other two negative diamonds of \(B\) then force, in particular,

\[
\epsilon_S(v_x)=\{0,x-1\}.
\tag{3.1}
\]

Direct cyclic reduction gives the following first-survivor table. Each row
lists \(p_+(S+v_x)\) as \(y\) runs through \(R_x\) in increasing order:

\[
\begin{array}{c|c|c|c}
x&R_x&v_x&\bigl(p_+(S+v_x)\bigr)_{y\in R_x}\\ \hline
3&\{1,5,7,9\}&4&(3,6,8,3)\\
5&\{1,3,7,9\}&6&(5,5,8,5)\\
7&\{1,3,5,9\}&8&(7,7,7,7)\\
9&\{1,3,5,7\}&9&(2,4,6,8).
\end{array}
\tag{3.2}
\]

None can give the pair \(\{0,x-1\}\). In the sole entry where the displayed
survivor equals \(x-1\), namely \(x=9,y=7\), the other survivor is \(6\),
so the pair is \(\{6,8\}\), not \(\{0,8\}\).

For the boundary \(x=1\), put

\[
Y=R_1+2=\{2,3,5,7,9\}.
\]

A completing alpha would require

\[
\epsilon_{Y-y}(10)=\{0,1\}
\qquad(y\in Y).
\tag{3.3}
\]

Instead,

\[
\begin{array}{c|ccccc}
y&2&3&5&7&9\\ \hline
\epsilon_{Y-y}(10)
&\{0,2\}&\{3,4\}&\{4,6\}&\{6,8\}&\{1,8\}.
\end{array}
\tag{3.4}
\]

Thus no single-cancellation completion exists.

## 4. Double cancellation at the shared row is impossible

For \(x\in\{3,5,7,9\}\), the positive diamond of \(A\) opposite \(d_x\) at
\(Y_x\) has pair \(\{0,x\}\). If both diamonds at \(Y_x\) cancel, then \(B\)
has positive pair \(\{0,x-1\}\) and negative pair \(\{0,x\}\) there.
Consequently its two other negative diamonds require

\[
\epsilon_{Y_x-y}(x)=\{0,x-1\},
\qquad
\epsilon_{Y_x-y}(x-1)=\{0,y\}.
\tag{4.1}
\]

The first row in (4.1) is \(Z-y+10\). Its endpoint pair depends only on
\(y\), and exact cyclic reduction gives

\[
\begin{array}{c|ccccc}
y&1&3&5&7&9\\ \hline
\epsilon(Z-y+10)
&\{0,2\}&\{2,4\}&\{4,6\}&\{6,8\}&\{8,9\}.
\end{array}
\tag{4.2}
\]

Equality with \(\{0,x-1\}\) is possible only for \(x=3,y=1\). In that one
case the second row in (4.1) is

\[
(Y_3-1)+2=\{2,5,7,9,10\},
\]

whose endpoint pair is \(\{0,4\}\), not \(\{0,1\}\).

At the boundary \(x=1\), double cancellation would again require the first
condition (3.3), already excluded by (3.4).

Therefore no double-cancellation completion exists.

## 5. Conclusion

Sections 1--4 exhaust every different-core sum of two formal alphas whose
surviving negative side contains the alternating PBBS chord. Reflection
handles the spare-\(10\) cases. Hence:

### Theorem 5.1

No changing-core two-alpha commutator is an executable portal from the
alternating component of the \(k=11\) complemented PBBS factor.

Combining this with the same-core \(K_4\) classification yields

\[
\boxed{\text{every alpha-generated portal uses at least three formal
alphas}.}
\]

This is a lower bound only. It does not construct a three-alpha portal and
does not exclude a non-alpha primitive circuit outside the local sigma-trade
model.

## 6. Relation to the equivariant sigma CSP

This obstruction is seed-specific. It constrains the endpoint table of the
PBBS factor, not an arbitrary solution of the \(42\)-variable
\(\mathbb Z_{11}\)-equivariant sigma CSP.

The two frameworks nevertheless meet as follows:

- an alpha trade preserves every lower, middle, and upper marginal, so an
  orbit of eleven translated alpha trades preserves equivariance, the
  degree-two constraints, and surjectivity of an equivariant sigma solution;
- a single local portal generally breaks equivariance;
- an orbit-summed portal can change the quotient component structure, but
  whether it turns a quotient cycle into one nonzero-voltage lifted cycle is
  an additional voltage calculation.

Thus the CSP can bypass the PBBS portal obstruction by constructing the
Hamilton cycle directly. If it returns only an equivariant 2-factor, the
trade machinery remains relevant, but only through full translation-orbits
of trades and with voltage tracked explicitly.
