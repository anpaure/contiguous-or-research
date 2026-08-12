# Audit of the proposed (k=11) PBBS portal commutator

Date: 2026-07-27

Method: exact set calculations only; no computation or search.

## 0. Verdict

Both proposed local switches are legal, and each preserves the complete
rank-five, rank-six, and rank-seven q1 marginal vectors exactly.  The first
octahedral four-trade changes the chord labelled by the alternating row

\[
 Z=\{1,3,5,7,9\}
\]

from endpoint pair \(\{0,10\}\) to \(\{0,2\}\).  The stated second alpha
side then really exists.

Nevertheless the composition does **not** touch the alternating component
at its alpha step.  The four-trade is a port transporter: it moves the
\(Z\)-labelled chord off the alternating component while putting its new
row-(10) and row-(2) chords onto that component.  The subsequent alpha
uses the migrated \(Z\)-labelled chord, not either transported alternating
route edge.

Thus the proposal proves a q1-exact local commutator, but not Gate A.  A
corrected portal alpha must contain one of the transported row-(10) or
row-(2) edges, or another edge known from the external-port trace to remain
on the alternating route.

## 1. First endpoint chart

Put

\[
 R=Z-\{1\}=\{3,5,7,9\},
 \qquad Q=\{0,1,2,10\}.
\]

Direct cyclic reduction gives

\[
\begin{array}{c|c}
x&\epsilon_R(x)\\ \hline
1&\{0,10\}\\
10&\{0,2\}\\
0&\{1,2\}\\
2&\{1,10\}.
\end{array}
\tag{1.1}
\]

For \(C_x=R+x\) and \(U_y=R+(Q-y)\), the omitted-upper assignment is

\[
 1\mapsto2,
 \quad2\mapsto0,
 \quad0\mapsto10,
 \quad10\mapsto1.
\tag{1.2}
\]

It is the directed four-cycle \((1,2,0,10)\).  Replacing it by its reverse
is exactly the octahedral four-cycle circulation.  The new endpoint table is

\[
\begin{array}{c|c}
x&\epsilon'_R(x)\\ \hline
1&\{0,2\}\\
10&\{1,2\}\\
0&\{1,10\}\\
2&\{0,10\}.
\end{array}
\tag{1.3}
\]

The K4 circulation theorem proves that (1.2)--(1.3) preserve every lower
load, every middle degree, and every upper load.

## 2. The proposed alpha is locally valid

Put

\[
 R'=Z-\{5\}=\{1,3,7,9\},
 \qquad Q'=\{0,2,4,5\}.
\]

The rows \(R'+2\) and \(R'+4\) are untouched by the first switch.  Cyclic
reduction gives

\[
 \epsilon_{R'}(2)=\{0,4\},
 \qquad
 \epsilon_{R'}(4)=\{0,5\}.
\tag{2.1}
\]

Together with the changed chord

\[
 \epsilon'_{R'}(5)=\epsilon'_R(1)=\{0,2\},
\tag{2.2}
\]

the three pairs are

\[
 \{0,2\},\quad\{0,4\},\quad\{0,5\}.
\tag{2.3}
\]

They form an alpha side with common spare (0) and rotating coordinates
\((5,2,4)\).  The alpha circulation therefore preserves the same three q1
marginals exactly.  There is no local-containment or colour error in the
proposal.

## 3. Exact external-port trace of the four-trade

Suppress the common core (R) and denote a central six-set by its two
coordinates from (Q).  Before the switch, the four selected chords are

\[
\begin{array}{c|c}
\text{row}&\text{central edge}\\ \hline
1&01--1\,10\\
0&01--02\\
10&0\,10--2\,10\\
2&12--2\,10.
\end{array}
\tag{3.1}
\]

Hence their old internal paths are

\[
 1\,10--01--02,
 \qquad
 0\,10--2\,10--12.
\tag{3.2}
\]

The first path uses rows (1) and (0).  These are precisely the two
successive alternating rows (Z) and (Z+2), so (3.2)'s first path lies on
the alternating PBBS component.

After the four-trade, the selected chords are

\[
\begin{array}{c|c}
\text{row}&\text{central edge}\\ \hline
1&01--12\\
0&01--0\,10\\
10&1\,10--2\,10\\
2&02--2\,10.
\end{array}
\tag{3.3}
\]

Their new paths are

\[
 1\,10--2\,10--02,
 \qquad
 0\,10--01--12.
\tag{3.4}
\]

Thus the external pairing is unchanged, as required by four-trade
inertness, but the row ownership of the two routes is exchanged:

\[
 \boxed{
 \text{alternating route: old rows }\{1,0\}
 \longrightarrow
 \text{new rows }\{10,2\}.}
\tag{3.5}
\]

In particular, after the switch the new row-(1), or (Z)-labelled, chord
\(01--12\) lies on the *other* old component.

## 4. Component consequence for the alpha

The second alpha cuts the rows

\[
 Z,
 \qquad R'+2=\{1,2,3,7,9\},
 \qquad R'+4=\{1,3,4,7,9\}.
\tag{4.1}
\]

The last two are neither of the transported rows in (3.5), and neither is
an alternating translate.  The first is the migrated (Z)-labelled chord,
which (3.5) has moved off the alternating component.  Therefore none of the
three alpha cuts lies on the alternating component.

The action profiles of the two untouched partner rows are respectively

\[
 (3,1,1),qquad(4,1),
\tag{4.2}
\]

but this does not restore the missing contact: profile information labels
the original PBBS components, whereas the four-trade has already transported
the (Z)-edge between routes.  Depending on the remaining phase data, the
alpha may be a ternary merge or a binary interlacement on nonalternating
components.  Its exact component derivative is irrelevant to Gate A and is
not proved here.

## 5. Exact residual gate

The construction demonstrates why lower-row labels cannot be used as
component labels after a component-inert octahedral switch.  The corrected
finite target is:

> Starting from (1.3), find an alpha side containing the new row-(10) or
> row-(2) chord from the first path of (3.4), with its other two cuts on
> the required outside components and, in the binary case, the favourable
> retained-path interlacement.

Alternatively, use a larger marginal-preserving circuit whose contracted
port graph connects the alternating external route directly to another
component.  Any candidate must be audited by its external-port pairing,
not merely by which lower-row labels occur in its support.

## 6. Neither transported edge has an alpha portal

The obstruction persists one step further.  Let

\[
 Y=R+2=\{2,3,5,7,9\},
 \qquad
 W=R+10=\{3,5,7,9,10\}.
\]

After the four-trade their endpoint pairs are respectively
\(\{0,10\}\) and \(\{1,2\}\), and these are the two edges on the
transported alternating route in (3.4).

For every deleted coordinate \(x\in Y\), put \(S=Y-x\).  An alpha through
the row \(Y\) must use spare (0) or (10).  The first forced partner
checks are as follows; an arrow records the sole boundary case in which the
first partner contains the spare and hence forces a third row.

\[
\begin{array}{c|cc}
x&\text{spare }0&\text{spare }10\\ \hline
2&\{1,2\}\not\ni0&\{1,10\}\to\{0,2\}\not\ni10\\
3&\{3,4\}\not\ni0&\{3,4\}\not\ni10\\
5&\{4,6\}\not\ni0&\{4,6\}\not\ni10\\
7&\{6,8\}\not\ni0&\{6,8\}\not\ni10\\
9&\{1,8\}\not\ni0&\{10,8\}\to\{1,9\}\not\ni10.
\end{array}
\tag{6.1}
\]

Every pair in (6.1) is obtained by direct cyclic reduction of the indicated
rank-five row.  Thus (Y) lies in no post-switch alpha chart.

For every \(x\in W\), the analogous table is

\[
\begin{array}{c|cc}
x&\text{spare }1&\text{spare }2\\ \hline
3&\{0,4\}\not\ni1&\{2,4\}\to\{0,3\}\not\ni2\\
5&\{4,6\}\not\ni1&\{4,6\}\not\ni2\\
7&\{6,8\}\not\ni1&\{6,8\}\not\ni2\\
9&\{1,8\}\to\{0,2\}\not\ni1&\{8,9\}\not\ni2\\
10&\{0,10\}\not\ni1&\{0,2\}\to\{1,10\}\not\ni2.
\end{array}
\tag{6.2}
\]

Hence (W) also lies in no post-switch alpha chart.  The alternating
component remains an isolated vertex of the alpha-support hypergraph after
this particular port transport.

## 7. One more overlapping K4 does not continue the route

The same endpoint tables classify K4 charts containing (Y) or (W).
For a four-trade through a row with endpoint pair \(\{a,b\}\), deleting a
row coordinate (x) forces the four-coordinate set
\(\{x,a,b,y\}\) for one further coordinate (y).  Substitution in
(6.1)--(6.2) shows:

* for (Y), every (x\notin\{2,3\}) produces two endpoint labels outside
  the forced four-set; (x=3) gives two disjoint transpositions rather than
  a four-cycle; and (x=2) gives exactly the inverse of the first
  four-trade;
* for (W), the same conclusion holds, with (x=9) failing at its fourth
  row and (x=10) giving the inverse trade.

Therefore no noninverse octahedral four-trade containing either transported
alternating edge is present after the first switch.

This proves a sharp verdict for the proposed direct-overlap strategy:

\[
 \boxed{
 \text{one K4 transport creates neither an alpha portal nor a second
 noninverse K4 transport on the alternating route}.}
\tag{7.1}
\]

It does not exclude a move on disjoint partner rows which later creates a
portal, nor a larger K5/K6-support circuit.  Those are now the smallest open
possibilities.
