# Lane K: corrected terminal-sector transport and the false shared-fusion premise

Date: 2026-07-25

Pure mathematics only. No computation, finite search, or external input is
used.

## 0. Outcome

Let \(D\) be a semilength-\(r\) Dyck root of height \(h\), and decompose
its first deepest spine as

\[
 D=A_0\,1A_1\,1\cdots1A_{h-1}\,1\,0B_{h-1}0\cdots0B_1\,0B_0.
 \tag{0.1}
\]

The proposed shared fusion of all primitive, or all terminal-maximum,
sectors cannot be based on the advertised cyclic sector shift.  The
hypothesis \(B_0=\varnothing\) makes only the *first* formal shift legal; it
does not keep the displayed spine canonical in later shifts.

This note identifies the exact protected class for that particular
\(h\)-round sector transport.  Write \(\operatorname{ht}(F)\) for the
maximum relative height of a component of an ordered forest, with the empty
forest having height zero.  The formal sector itinerary remains the
canonical first-deepest-spine itinerary through rounds \(0,\ldots,h\) if
and only if

\[
 \boxed{
 A_k=\varnothing\quad(0\le k<h),
 \qquad \operatorname{ht}(B_k)\le k\quad(0\le k<h).
 }
 \tag{0.2}
\]

The usual original-height constraint also gives
\(\operatorname{ht}(B_k)\le h-k\).  In particular (0.2) forces
\(B_0=\varnothing\).  On this protected class the sector computation is
valid and gives a first zero-winding return of gap \(2h+1\).

However, if \(\mathcal S_r\) denotes the union of this protected class over
all heights, then for an absolute \(c>0\),

\[
 \boxed{
 |\mathcal S_r|\le r4^r e^{-c r^{1/3}}
 =o\!\left(\operatorname{Cat}_r/r^K\right)
 \quad\hbox{for every fixed }K.
 }
 \tag{0.3}
\]

Consequently, for \(H=O_A(\sqrt r)\), even paying the old full
\((H^2+2H)\)-per-cut endpoint-cap plus literal-repair bill at every physical
lift of every protected root costs

\[
 (2r+1)(H^2+2H)|\mathcal S_r|=o_A(W),
 \qquad W=(2r+1)\operatorname{Cat}_r.
 \tag{0.4}
\]

Thus no shared braid is needed on the largest class justified by the
first-deepest-spine sector atlas.  Conversely, that atlas gives no literal
ports for all primitive roots: the explicit primitive root
\(1110011000\) sends the alleged return coordinate to a different physical
label.  A successful nonlocal fusion, if needed for the true PBBS return
family, must follow the exact block rotation \(\tau D=S1P0R\) through its
frame changes.  It cannot group all primitive roots by the static sector
table (0.1).

This is an exact obstruction to the requested fusion architecture, not a
proof that every possible orbitwise PBBS braid is impossible.

## 1. One exact shift and the formal sector table

At the first up-step reaching the maximum write

\[
 D=P\,1\,R\,0\,S.
\]

For (0.1),

\[
\begin{aligned}
 P&=A_0\,1A_1\cdots1A_{h-1},\\
 R&=0B_{h-1}0\cdots0B_1,\\
 S&=B_0.
\end{aligned}
\tag{1.1}
\]

Hence the exact two-step quotient map is

\[
 \tau D=B_0\,1A_0\,1A_1\cdots1A_{h-1}\,0\,0B_{h-1}0\cdots0B_1.
 \tag{1.2}
\]

If the displayed old spine is still the canonical first deepest spine,
the one-round sector update is

\[
 A'_0=B_0,qquad A'_i=A_{i-1}\ (1\le i<h),
 \tag{1.3}
\]

and

\[
 B'_i=B_{i+1}\ (0\le i<h-1),qquad B'_{h-1}=\varnothing.
 \tag{1.4}
\]

Iterating these *formal* updates gives

\[
 A_i^{[j]}=
 \begin{cases}
 B_{j-1-i},&i<j,\\
 A_{i-j},&i\ge j,
 \end{cases}
 \qquad
 B_i^{[j]}=
 \begin{cases}
 B_{i+j},&i+j<h,\\
 \varnothing,&i+j\ge h.
 \end{cases}
 \tag{1.5}
\]

The brackets emphasize that these are initially only formal sectors.  They
are canonical precisely when every forest appearing before the displayed
spine stays strictly below total height \(h\).

## 2. Exact protection criterion

### Theorem 2.1 (canonicality of the full formal itinerary)

The formal sectors (1.5) are the canonical first-deepest-spine sectors of
\(\tau^jD\) for every \(0\le j\le h\) if and only if (0.2) holds.

#### Proof: sufficiency

Assume (0.2).  An original \(A_k\) contributes nothing.  If an original
\(B_k\) occurs in an \(A\)-sector at round \(j\), (1.5) puts it at depth

\[
 i=j-1-k.
\]

Therefore every leaf in that forest has total depth at most

\[
 i+\operatorname{ht}(B_k)
 \le j-1-k+k=j-1<h.
 \tag{2.1}
\]

Thus no forest preceding the displayed spine reaches height \(h\).  The
displayed spine itself still reaches height \(h\), so it remains the first
deepest spine.

Forests in the formal \(B\)-sectors occur after that spine.  The original
height constraint

\[
 \operatorname{ht}(B_k)\le h-k
 \tag{2.2}
\]

shows directly from (1.5) that they do not exceed height \(h\); ties are
allowed after the first deepest leaf.  Hence the formal update is canonical
at every round, proving sufficiency.

#### Proof: necessity

Suppose first that some \(A_k\) is nonempty.  Necessarily \(k\le h-2\),
because \(A_{h-1}=\varnothing\).  At round

\[
 j=h-1-k,
\]

formula (1.5) places \(A_k\) in the formal \(A_{h-1}\)-sector.  A nonempty
forest has relative height at least one, so it reaches total height at least
\(h\) before the displayed terminal spine edge.  The displayed spine is
therefore no longer the first deepest spine.  Full canonicality forces all
\(A_k\) to be empty.

Now suppose \(\operatorname{ht}(B_k)\ge k+1\).  At round \(j=h\), formula
(1.5) places \(B_k\) in the formal \(A_{h-1-k}\)-sector.  Its total height
is at least

\[
 (h-1-k)+(k+1)=h,
\]

again before the displayed spine.  Thus the round-\(h\) formal frame is not
canonical.  Full canonicality forces
\(\operatorname{ht}(B_k)\le k\) for every \(k\).  This proves necessity.
\(\square\)

The terminal condition \(B_0=\varnothing\) is therefore only the
\(k=0\) member of a whole triangular system of protection inequalities.

## 3. Return law on the protected class

For a canonical first-maximum decomposition put

\[
 d(D)=2|B_0|+1,
 \qquad
 \delta(D)=h+2\sum_{i=0}^{h-1}|A_i|.
 \tag{3.1}
\]

Let \(D_j=\tau^jD\) for a protected root.  From (1.5),

\[
 d(D_j)=2|B_j|+1\qquad(0\le j<h),
 \tag{3.2}
\]

and

\[
 \delta(D_j)=h+2\sum_{t=0}^{j-1}|B_t|
 \qquad(0\le j\le h).
 \tag{3.3}
\]

Put \(C_j=\sum_{t<j}d(D_t)\).  Then

\[
 C_j=j+2\sum_{t<j}|B_t|,
 \tag{3.4}
\]

so

\[
 \delta(D_j)-C_j=h-j>0\quad(j<h),
 \qquad
 \delta(D_h)=C_h.
 \tag{3.5}
\]

The exact PBBS skew product places the even-time root at \(u-C_j\pmod N\),
and the next odd step adds \(\delta(D_j)\).  Equation (3.5) therefore gives
a return at time \(2h+1\) and excludes every earlier odd time.  Moreover
\(0<C_j<C_h\le2r<N\) for \(0<j\le h\), so no earlier even time returns.
Thus the return is consecutive and zero-winding.

## 4. The protected family is stretched-exponentially sparse

Let \(s_{r,h}\) be the number of protected semilength-\(r\) roots of height
\(h\).  There is first an exact product formula.  Let \(C_L(z)\) be the
generating function for Dyck forests of height at most \(L\), with

\[
 C_0(z)=1,\qquad C_L(z)={1\over1-zC_{L-1}(z)}.
\]

Since every \(A_i\) and \(B_0\) is empty, a protected root is uniquely

\[
 1^h0B_{h-1}0B_{h-2}\cdots0B_1 0,
\]

where

\[
 \operatorname{ht}(B_k)\le\min(k,h-k).
\]

The forests are independent and have total size \(r-h\).  Therefore

\[
 \boxed{
 s_{r,h}=[z^{r-h}]
 \prod_{k=1}^{h-1}C_{\min(k,h-k)}(z).
 }
 \tag{4.1}
\]

For the uniform bound, it is enough to use two simpler relaxations.  Since
every \(A_i\) is empty, (0.1) begins with \(h\) consecutive
up-steps.  Forgetting Dyck nonnegativity after that prefix gives

\[
 s_{r,h}\le {2r-h\choose r-h}\le2^{2r-h}=4^r2^{-h}.
 \tag{4.2}
\]

Independently, every such root has height at most \(h\).  The path-graph
spectral-radius bound gives

\[
 s_{r,h}
 \le \left(2\cos{\pi\over h+2}\right)^{2r}
 \le4^r\exp\!\left(-{\pi^2r\over(h+2)^2}\right).
 \tag{4.3}
\]

For \(r\ge64\), either \(h\ge r^{1/3}/2\), in which case (4.2) has loss
at least \((\log2)r^{1/3}/2\), or \(h<r^{1/3}/2\), in which case
\(h+2\le r^{1/3}\) and (4.3) has loss at least \(\pi^2r^{1/3}\).
Consequently, with \(c=(\log2)/2\),

\[
 s_{r,h}\le4^r e^{-c r^{1/3}}
 \qquad(r\ge64).
 \tag{4.4}
\]

Summing over at most \(r\) heights proves the first inequality in (0.3).
The Wallis bounds

\[
 \operatorname{Cat}_r\ge c_0 4^r r^{-3/2}
\]

then give

\[
 { |\mathcal S_r|\over\operatorname{Cat}_r}
 \le C r^{5/2}e^{-c r^{1/3}}
 =o(r^{-K})
\]

for every fixed \(K\), proving (0.3).

For every fixed \(A\), \(H\le A\sqrt r+1\) gives \(H^2+2H=O_A(r)\).
There are at most \(N=2r+1\) physical lifts per quotient root.  Hence the
old quadratic literal-repair charge over the entire protected class is at
most

\[
 N(H^2+2H)|\mathcal S_r|.
\]

Dividing by \(W=N\operatorname{Cat}_r\) and applying (0.3) proves (0.4).

## 5. Literal endpoint failure outside the protected class

Take

\[
 D_0=1110011000,qquad N=11.
\]

It is primitive, has height three, and has \(B_0=\varnothing\).  Exact
applications of \(\tau D=S1P0R\) give

\[
\begin{array}{c|c|c}
 D_j&\delta(D_j)&d(D_j)\\ \hline
1110011000&3&1\\
1110001100&3&5\\
1100111000&7&1,
\end{array}
\qquad D_3=D_0.
\tag{5.1}
\]

Thus after three two-step moves the spatial root is \(u-7\), while the
following odd move adds only \(3\).  The endpoint label is

\[
 u-7+3=u-4\not\equiv u\pmod {11}.
 \tag{5.2}
\]

The alleged height-three return ports therefore carry two different
physical labels.  A splice or braid which identifies those ports does not
repair a coordinate residence: it joins the insertion of one coordinate to
an event involving another.  This is a literal factor-consistency failure,
not merely a bad estimate.

For completeness, the accumulated deficits through six two-step moves are

\[
 C_j=0,1,6,7,8,13,14\qquad(0\le j\le6),
\]

whereas

\[
 \delta(D_j)=3,3,7,3,3,7,3.
\]

Modulo eleven, no positive even-time value \(C_j\) is zero, and
\(C_j\not\equiv\delta(D_j)\) for \(0\le j<6\).  At \(j=6\), however,
\(C_6=14\equiv3=\delta(D_6)\pmod {11}\).  Thus the first genuine return
has gap \(13\), not the predicted \(7\).

## 6. Precise boundary

The report proves the following.

1. The full \(h\)-round first-deepest-sector atlas has the exact protection
   criterion (0.2).
2. Every protected root has the advertised exact return, but all protected
   roots together are stretched-exponentially sparse and can be repaired
   independently at \(o(W)\) total cost in a fixed Gaussian band.
3. Primitive and terminal-maximum roots outside that class do not share the
   alleged sector ports.  The explicit primitive root (5.1) gives a literal
   endpoint-label obstruction.

It does **not** prove that \((RP_A)\) holds, nor that \((RP_A)\) fails.  It
does **not** exclude a braid indexed by the complete exact \(\tau\)-orbit,
by peak-deletion passage data, or by some other frame-changing invariant.
It shows that the proposed positive-density fusion cannot be obtained by
iterating the static first-deepest-spine sector shift over all primitive or
all \(B_0=\varnothing\) roots.
