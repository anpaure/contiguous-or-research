# Lane H: a deadline-exact, seam-relaxed four-sector \(k\mapsto k+2\) induction theorem

Date: 2026-07-28

Method: pure mathematics only. No finite search, solver, or web input is
used.

## 0. Verdict

There is no presently proved implication

\[
 \nu(k)=B(k)\quad\Longrightarrow\quad \nu(k+2)=B(k+2).
\]

The four-sector diamond construction does, however, admit an exact
fail-closed induction theorem. This note proves four ingredients.

1. For odd \(k=2r-1\), the new monotone-deadline depth is always either
   \(d(k)\) or \(d(k)+1\), with a sharp Catalan-slack criterion deciding
   which.
2. An endpoint-rooted, one-hole lower-rainbow carrier whose completed first
   lower row is second-shadow complete supplies an exact Catalan forest in
   the both-new sector: it has precisely \(C_r\) components and uses every
   required immediate lower colour once.
3. Johnson adjacency is not required at every new seam. A seam of swap
   distance \(s\) gives a rank-depth-\(s\) upper union and offers the
   corresponding lower intersection in the maximal erosion; that lower cell
   survives only if it is pinned through the compiler. The seam is legal
   whenever residence, cross-depth upper support, and the lower compiler
   survive. This is the precise seam relaxation.
4. After the middle deck has been ordered, the remaining obligations split
   exactly into:

   \[
   \boxed{\text{new-depth residence}}
   \quad+
   \boxed{\text{cross-depth transferred upper support}}
   \quad+
   \boxed{\text{pin-compatible sandwich Hall}}.
   \]

The first Catalan forest is automatic under the stated old-carrier
hypotheses. The simultaneous ordering satisfying the three boxed conditions
is **unproved**. In particular, neither the Catalan component count nor
scalar deadline slack implies any of the three labelled conditions.

Thus the strongest rigorous conclusion is a precise induction theorem and a
minimal three-gate obstruction, not a proof of the all-\(k\) formula.

## 1. Exact deadline arithmetic

Let

\[
 k=2r-1,\qquad W=\binom{2r-1}{r},
 \qquad \Lambda=\sum_{j=1}^{r-1}\binom{2r-1}{j}.
\]

Since the ground set is odd,

\[
 \Lambda=2^{2r-2}-1.
\tag{1.1}
\]

Write

\[
 T_d=\binom{d+1}{2},
 \qquad
 d=d(2r-1)=\min\{t:tW+T_t\ge\Lambda\},
\]

and let

\[
 \sigma=dW+T_d-\Lambda
\tag{1.2}
\]

be the old deadline slack.

After adjoining two coordinates, the new central width and lower demand are

\[
 W^+=\binom{2r+1}{r+1},
 \qquad
 \Lambda^+=\sum_{j=1}^{r}\binom{2r+1}{j}.
\]

Put

\[
 b:=\frac{2W}{r+1}=C_r.
\tag{1.3}
\]

The exact four-sector identities are

\[
 \boxed{W^+=4W-b},
 \qquad
 \boxed{\Lambda^+=4\Lambda+3}.
\tag{1.4}
\]

The first follows from

\[
 \frac{W^+}{W}=\frac{2(2r+1)}{r+1}=4-\frac2{r+1};
\]

the second follows from (1.1).

### Theorem 1.1 (deadline--Catalan recurrence)

For every \(r\ge2\),

\[
 d(2r+1)\in\{d,d+1\}.
\tag{1.5}
\]

More precisely,

\[
\boxed{
 d(2r+1)=d
 \iff
 4\sigma\ge db+3T_d+3.}
\tag{1.6}
\]

If (1.6) fails, then \(d(2r+1)=d+1\).

The new slack is consequently

\[
 \sigma^+=
 \begin{cases}
 4\sigma-db-3T_d-3,&d(2r+1)=d,\\[2mm]
 4\sigma-db-3T_d+W^++d-2,&d(2r+1)=d+1.
 \end{cases}
\tag{1.7}
\]

#### Proof

First, the minimality of \(d\) gives

\[
 (d-1)W+T_{d-1}<\Lambda.
\]

Since \(W^+<4W\),

\[
 (d-1)W^++T_{d-1}
 \le4(d-1)W+4T_{d-1}<4\Lambda<\Lambda^+.
\]

Thus \(d(2r+1)\ge d\).

Next, \(d\le r-1\), because \(\Lambda\) is a sum of \(r-1\) binomial
coefficients, each at most \(W\). Using \(\Lambda\le dW+T_d\), it is
enough for the upper bound to prove

\[
 (d+1)W^++T_{d+1}\ge4dW+4T_d+3.
\tag{1.8}
\]

The difference between the two sides is

\[
 S(d)=
 \left(4-\frac{2(d+1)}{r+1}\right)W
 +\frac{(d+1)(2-3d)}2-3.
\tag{1.9}
\]

Indeed

\[
 S(d+1)-S(d)=-\frac{2W}{r+1}-3d-2<0.
\]

Thus its minimum on
\(0\le d\le r-1\) occurs at \(d=r-1\). There

\[
 S(r-1)=
 \left(2+\frac2{r+1}\right)W
+\frac{-3r^2+5r-6}{2}.
\tag{1.10}
\]

For \(r=2\), this is positive directly. For \(r\ge3\),

\[
 W=\binom{2r-1}{r-1}\ge\binom{r+2}{3}.
\tag{1.11}
\]

Indeed equality holds at \(r=3\), and the ratio on the left when \(r\)
is increased by one is

\[
 \frac{2(2r+1)}{r+1},
\]

which is at least the corresponding ratio \((r+3)/r\) on the right.
The lower bound (1.11) makes (1.10) nonnegative, since

\[
 2\binom{r+2}{3}\ge\frac{3r^2-5r+6}{2}.
\]

Hence (1.8) holds, proving (1.5).

Finally, substituting (1.2) and (1.4) gives

\[
 dW^++T_d-\Lambda^+
 =4\sigma-db-3T_d-3.
\tag{1.12}
\]

Thus depth \(d\) works exactly under (1.6). If it fails, (1.5) forces
depth \(d+1\). Adding \(W^++d+1\) to (1.12) gives the second line of
(1.7). \(\square\)

The identity (1.12) is the exact scalar cost of deleting one Catalan batch
of \(b\) middle positions while trying to reuse four old deadline profiles.
It is not a Hall theorem.

## 2. The four sectors and the lower-demand split

Add new coordinates \(x,y\), and put \(R=r+1\) for the new middle rank.
The new middle layer decomposes into

\[
\begin{array}{c|c|c}
\text{sector}&\text{set}&\text{cardinality}\\ \hline
A&C\cup\{x,y\},\quad |C|=r-1&W\\
X&T\cup\{x\},\quad |T|=r&W\\
Y&T\cup\{y\},\quad |T|=r&W\\
U&V,\quad |V|=r+1&W-b.
\end{array}
\tag{2.1}
\]

This proves the first identity in (1.4) directly.

The lower targets also have an exact four-way split according to their new
coordinate set:

\[
\begin{array}{c|c}
S\cap\{x,y\}&\#\{S:1\le |S|<R\}\\ \hline
\varnothing&\Lambda+W\\
\{x\}&\Lambda+1\\
\{y\}&\Lambda+1\\
\{x,y\}&\Lambda+1-W.
\end{array}
\tag{2.2}
\]

For example, the both-new line is

\[
 \sum_{j=0}^{r-2}\binom{2r-1}{j}=\Lambda+1-W.
\]

Summing (2.2) gives \(4\Lambda+3\), the second identity in (1.4).

More generally, if a new target has signed depth \(q\) from the new middle
rank and uses \(s\in\{0,1,2\}\) new coordinates, then its old projection
has signed depth

\[
 \boxed{q+1-s}
\tag{2.3}
\]

from the old rank-\(r\) middle layer. Here upper depth is positive and lower
depth is negative. In particular, a new immediate lower target containing
both \(x,y\) projects to an old depth-two lower target. This is why the
second old lower shadow, rather than only the immediate one, is the first
nontrivial Catalan input.

### Theorem 2.1 (an exact deadline-safe sector skeleton)

Assume \(r\ge3\). There is a cyclic unlabelled sector word

\[
 U_1Y_1A_1X_1\ U_2Y_2A_2X_2\cdots U_bY_bA_bX_b
\tag{2.4}
\]

with \(b=C_r\) nonempty blocks of each sector, the exact sector totals
\((W,W,W,W-b)\), and every \(x\)-run and every \(y\)-run of length exactly
\(r+1\). Its cyclic immediate-lower eligible-position census is exactly

\[
\begin{array}{c|c}
\text{new-bit type}&\text{eligible positions}\\ \hline
\{x,y\}&W-b\\
\{x\}&W\\
\{y\}&W\\
\varnothing&W.
\end{array}
\tag{2.5}
\]

Since Theorem 1.1 gives \(d^+\le r\), every new-coordinate run in (2.4)
meets the exact residence requirement \(d^++1\le r+1\).

#### Proof

Choose positive integers \(a_i\le r\) with

\[
 \sum_{i=1}^{b}a_i=W.
\]

This is possible because \(W/b=(r+1)/2\). Put

\[
 |A_i|=a_i,qquad |X_i|=|Y_i|=r+1-a_i.
\]

Then

\[
 \sum_i|X_i|=\sum_i|Y_i|=b(r+1)-W=W.
\]

Also \((W-b)/b=(r-1)/2\ge1\), so positive \(U\)-block lengths summing
to \(W-b\) exist. In (2.4), the \(x\)-runs are the strings \(A_iX_i\)
and the \(y\)-runs are \(Y_iA_i\), both of length \(r+1\).

There are \(W-b\) internal edges in each of \(A,X,Y\), and \(W-2b\)
internal edges in \(U\). The cyclic seams contribute \(b\) edges of each
type \(UY,YA,AX,XU\). Hence the four eligible-position counts are

\[
 AA=W-b,
\]

\[
 XX+AX=W-b+b=W,
 \qquad YY+YA=W,
\]

and

\[
 UU+UY+XU=(W-2b)+2b=W.
\]

This proves (2.5). If every counted labelled adjacency is Johnson, these
eligible positions become the corresponding q1 slots. \(\square\)

The word “unlabelled” is essential: Theorem 2.1 proves that neither sector
cardinalities nor the two new-coordinate deadlines obstruct induction. It
does not assign actual middle sets to the positions or make the displayed
seams Johnson. Cutting the cycle into a Hamilton path deletes one eligible
position of the cut's signature. Only after the labels are rainbow and the
lost colour is endpoint-compatible can a boundary flag absorb that loss.

## 3. An exact Catalan forest supplied by an old carrier

Let

\[
 P=(T_0,\ldots,T_{W-1})
\]

be a Hamilton path in \(J(2r-1,r)\). Put

\[
 C_i=T_i\cap T_{i+1}\qquad(0\le i<W-1).
\]

Assume:

1. the \(C_i\) are distinct and omit exactly one
   \(C_*\in\binom{[2r-1]}{r-1}\);
2. after reversing \(P\) if necessary, \(C_*\subset T_0\); and
3. the completed path
   \[
   \widehat C=(C_*,C_0,C_1,\ldots,C_{W-2})
   \tag{3.1}
   \]
   has immediate intersections covering every member of
   \(\binom{[2r-1]}{r-2}\).

The first two assumptions make \(\widehat C\) a Hamilton path in
\(J(2r-1,r-1)\): consecutive members are distinct facets of the same
\(T_i\).

### Theorem 3.1 (Catalan batching without a selection loss)

There is a spanning path forest \(\mathcal F_A\) of \(\widehat C\) with
exactly

\[
 b=C_r
\]

components such that its edge intersections enumerate
\(\binom{[2r-1]}{r-2}\) exactly once. After adjoining \(x,y\) to every
vertex, the internal \(AA\) edges enumerate every new immediate lower
target containing both \(x,y\) exactly once.

#### Proof

There are

\[
 \binom{2r-1}{r-2}=\binom{2r-1}{r+1}=W-b
\tag{3.2}
\]

required colours. By assumption 3, choose one edge of \(\widehat C\) for
each colour. Retain precisely those \(W-b\) edges. They are distinct,
because one edge has only one intersection colour.

A subgraph of a path is a forest. It has \(W\) vertices and \(W-b\)
edges, hence exactly \(b\) components, isolated vertices included. The
chosen edge colours are the required layer exactly once. Adding \(x,y\)
to both endpoints changes each intersection \(R\) to
\(R\cup\{x,y\}\), proving the last claim. \(\square\)

Thus the no-waste Catalan count is a theorem once the completed second lower
shadow is available. No probabilistic batching or separate forest Hall
argument is needed.

For the other middle sectors, \(X\) and \(Y\) are two copies of \(P\).
If the immediate upper colours \(T_i\cup T_{i+1}\) cover every
rank-\((r+1)\) old set, then choosing one occurrence of each colour names
every vertex of \(U\). Therefore the old path supplies the complete new
middle **deck**. It still does not supply one valid global order of that
deck.

## 4. Necessary immediate-lower sector inequalities

Let \(T^+\) be any Hamilton ordering of the four-sector deck. Let \(b_S\)
be the number of maximal blocks of sector \(S\), let \(\epsilon_U\) be the
number of its two endpoints in \(U\), and let \(e_{ST}^{J}\) count only
Johnson transitions between sectors \(S,T\). Let \(t_J=e_{XY}^{J}\).

Write \(H_S^-\) for the number of missing immediate lower colours of the
new-bit type named by \(S\). Then

\[
\boxed{
\begin{aligned}
 H_A^-&\ge(b_A-b)^+,\\
 H_X^-&\ge(b_X-e_{AX}^{J})^+,\\
 H_Y^-&\ge(b_Y-e_{AY}^{J})^+,\\
 H_U^-&\ge(b-b_U-t_J+\epsilon_U)^+.
\end{aligned}}
\tag{4.1}
\]

#### Proof

There are \(W-b_A\) internal \(AA\) positions, and no other sector edge
can have an intersection containing both \(x,y\). There are \(W-b\)
such targets, proving the first inequality.

An \(x\)-only immediate lower target can occur only on a Johnson \(XX\)
or \(AX\) edge. There are at most \(W-b_X+e_{AX}^{J}\) such slots for
\(W\) targets. This proves the second inequality; the third is symmetric.

Finally, a neither-new immediate lower target can occur only on a Johnson
\(UU,XU,YU\), or \(XY\) edge. There are at most \(W-b-b_U\) internal
\(UU\) edges. The number of block-boundary incidences available to Johnson
\(XU\) and \(YU\) edges is at most \(2b_U-\epsilon_U\). Adding the
\(t_J\) Johnson \(XY\) edges gives at most

\[
 W-b+b_U-\epsilon_U+t_J
\]

slots for \(W\) targets, proving the fourth inequality. Non-Johnson seams
were deliberately not credited. \(\square\)

If \(T^+=D^{d^+}A\) for a universal word, at most two missing immediate
lower colours can be supplied away from the rank-\((R-1)\) intersections of
consecutive middle cells. To see this, a rank-\((R-1)\) witness has length
at most \(d^+\), since a longer interval contains a complete central window
of rank \(R\). Every nonboundary short cell is contained in two consecutive
central windows, hence its union is a subset of their intersection. If that
intersection has rank \(R-1\), equality is forced; if it has smaller rank,
the short cell cannot have rank \(R-1\). The only exceptions lie on the two
boundary anti-diagonals. Each anti-diagonal is nested and therefore contains
at most one distinct set of rank \(R-1\). Consequently a necessary condition
is

\[
 \sum_{S\in\{A,X,Y,U\}}H_S^-\le2.
\tag{4.2}
\]

Theorem 3.1 sets the first term of (4.1) to zero. The pure chronological
diamond ladder still has a degree-three conflict at its terminal
\(A(C_*)\): the final \(AA\) colour and the two colours
\(C_*\cup\{x\}\), \(C_*\cup\{y\}\) demand three distinct incident
edges. Thus one boundary hole is forced in that restricted graph. Condition
(4.2) shows why this is not fatal: the optimal compiler is allowed one or
two endpoint flags. Requiring a perfectly rainbow central path is stronger
than the actual induction theorem.

There is already a competing upper-q1 constraint. Put

\[
 P_0=\binom{2r-1}{r+2}.
\]

An empty-signature immediate upper target can only be witnessed on an
internal \(UU\) edge. Hence

\[
\boxed{b_U\le (W-b)-P_0}
\tag{4.3}
\]

is necessary for upper completeness. Combining (4.3) with the fourth line
of (4.1) shows why \(XY\) repair edges or a nonuniform sector-block profile
are genuinely needed. In particular, Theorem 2.1 is only a deadline-safe
and q1-capacity skeleton; its choice \(b_U=b\) need not satisfy (4.3).

## 5. Exact seam relaxation and residence

Put

\[
 d^+=d(2r+1).
\]

### Lemma 5.1 (rank-\(s\) seam identity)

Let consecutive new middle sets \(M,N\) have rank \(R\), and put

\[
 s=R-|M\cap N|.
\]

If \(T^+\) is depth-\(d^+\) resident and \(E\) is its maximal erosion,
then at this seam

\[
 (D^{d^+-1}E)_{i+1}=M\cap N,
 \qquad
 (DT^+)_i=M\cup N,
\tag{5.1}
\]

of ranks \(R-s\) and \(R+s\), respectively.

#### Proof

The second identity is the definition of \(D\). The first is the maximal
core identity

\[
 (D^{d^+-q}E)_{i+q}=\bigcap_{h=0}^{q}T^+_{i+h}
\]

at \(q=1\). The rank assertions follow from
\(|M|=|N|=R\). \(\square\)

A Johnson seam is the case \(s=1\). A seam with \(s=2\) sacrifices an
immediate lower and upper slot, gives an automatic rank-depth-two upper
union, and offers a rank-depth-two lower intersection in the maximal
erosion. A refinement \(A\subseteq E\) may shrink that lower cell, so it
must be explicitly pinned if the compiler uses it. Such a seam is legitimate
when the lost colours have other witnesses and all three global gates pass.
No argument may reject it merely because it is non-Johnson.

### Lemma 5.2 (piecewise residence criterion)

Cut proposed sector paths into oriented pieces and concatenate them. Assume
every coordinate run lying wholly in the interior of one piece has length at
least \(d^++1\). The concatenation is depth-\(d^+\) resident if and only if,
for every coordinate, each internal maximal run formed from terminal and
initial piece-runs across one or more seams has total length at least
\(d^++1\).

#### Proof

Every internal one-run of the concatenation is either wholly internal to one
piece or is the concatenation of a terminal run, zero or more all-one
pieces, and an initial run. These classes are disjoint and exhaustive. Apply
the exact binary residence criterion to each. \(\square\)

For the two new coordinates this becomes the especially transparent rule

\[
\boxed{
\begin{aligned}
 &\text{every internal maximal block string using only }A,X
   \text{ has total size at least }d^++1,\\
 &\text{every internal maximal block string using only }A,Y
   \text{ has total size at least }d^++1.
\end{aligned}}
\tag{5.2}
\]

For an old coordinate, Lemma 5.2 is the exact seam test; average Catalan
block length is irrelevant. In particular, if the deadline rises from
\(d\) to \(d+1\), every inherited internal run of length exactly \(d+1\)
must be cut or merged with a compatible boundary run. An old depth-\(d\)
carrier does not automatically meet the new depth.

There is a sharper obstruction on the chronological \(A\)-strand. For an
old coordinate \(z\), write

\[
 t_i=\mathbf1_{\{z\in T_i\}},
 \qquad
 c_i=\mathbf1_{\{z\in C_i\}}=t_it_{i+1}.
\]

An internal old run \(t_a=\cdots=t_b=1\) of length \(\ell=b-a+1\)
becomes the \(C\)-strand run \(c_a=\cdots=c_{b-1}=1\) of length
\(\ell-1\).

Let

\[
 D=d^++1.
\]

For every internal old run \([a,b]\), meaning
\(1\le a\le b\le W-2\), with \(2\le\ell\le D\), form the
interval of native \(C\)-spine edges

\[
 I_z(a,b)=
 \{C_{a-1}C_a,C_aC_{a+1},\ldots,C_{b-1}C_b\}.
\tag{5.3}
\]

Let \(\mathcal I_D(P)\) be the resulting interval family over all old
coordinates, and let \(\tau_D(P)\) be its maximum edge-disjoint
subfamily.

### Theorem 5.3 (chronological \(A\)-strand cut obstruction)

Every lift which keeps a native chronological \(A\)-edge unless that edge
is explicitly cut must cut at least one edge of every interval in
\(\mathcal I_D(P)\). Therefore it uses at least \(\tau_D(P)\) native
\(A\)-cuts. In the strict inherited Catalan batching architecture of
Theorem 3.1, with no additional \(AA\) rethreading,

\[
\boxed{\tau_D(P)\le b-1}
\tag{5.4}
\]

is necessary.

#### Proof

If no edge of (5.3) is cut, then the short binary word

\[
 0\,1^{\ell-1}\,0
\]

survives inside one \(A\)-piece, possibly reversed. Since
\(\ell-1<D\), the new chronology is not depth-\(d^+\) resident. Thus
the cut set is a transversal of \(\mathcal I_D(P)\). For intervals on a
line, the minimum transversal size equals the maximum number of pairwise
disjoint intervals: choose greedily the earliest right endpoint. This proves
the first assertion.

The exact Catalan forest has \(b\) components and is obtained from the
completed \(C\)-spine by deleting exactly \(b-1\) native edges. Hence
(5.4). \(\square\)

Hitting these intervals removes precisely the internally trapped short
\(A\)-runs; Lemma 5.2 must still be checked on the exposed boundary ports.
No non-Johnson seam outside an uncut piece can repair a short run trapped
inside it. Thus (5.4) is an architecture-specific but exact obstruction,
strictly stronger than an average block-length calculation.

A clean no-cut sufficient condition on the old chronology is that every old
internal one-run have length at least

\[
 D+1=d^++2.
\]

This is one unit stronger than old residence when \(d^+=d\), and two units
stronger when \(d^+=d+1\). It is sufficient only for the internal
\(A\)-strand issue; the port sums and the other strands remain.

## 6. Upper support: exact cross-depth transfer and collar accounting

Let the new ordering be a concatenation of oriented pieces

\[
 T^+=P_1P_2\cdots P_c.
\]

For \(q\ge1\), let \(I_q\) be the set of unions of length-\((q+1)\)
windows contained in a single piece and let \(N_q\) be the corresponding
set for windows crossing at least one new seam. Then, identically,

\[
 \boxed{\operatorname{supp}(D^qT^+)=I_q\cup N_q.}
\tag{6.1}
\]

This is the exact collar ledger: reversal preserves internal window unions,
all removed witnesses lie in cut collars, and every new witness lies in a
new seam collar.

For a rank offset \(t\ge1\) and signature \(B\subseteq\{x,y\}\), define

\[
\begin{aligned}
 \mathcal U^*_{t,B}(T^+)=
 \bigcup_{q\ge1}\bigg\{
 &\left(\bigcup_{j=0}^{q}T^+_{i+j}\right)\setminus\{x,y\}:\\
 &\left(\bigcup_{j=0}^{q}T^+_{i+j}\right)\cap\{x,y\}=B,
 \quad\left|\bigcup_{j=0}^{q}T^+_{i+j}\right|=R+t
 \bigg\}.
\end{aligned}
\tag{6.1a}
\]

### Proposition 6.1 (exact transferred-upper criterion)

For any factor \(A\) with \(D^{d^+}A=T^+\), the whole upper ideal is
covered if and only if

\[
\boxed{
 \mathcal U^*_{t,B}(T^+)
 =\binom{[2r-1]}{R+t-|B|}}
\tag{US*}
\]

for every nonempty target layer, every \(t\ge1\), and every signature
\(B\).

#### Proof

Every interval of \(A\) of length at most \(d^++1\) is contained in one
central window and hence has union of rank at most \(R\). Therefore an
upper target witness has length \(d^++q+1\) for some \(q\ge1\). If it
starts at \(i\), then

\[
 \bigcup_{h=0}^{d^++q}A_{i+h}
 =\bigcup_{j=0}^{q}T^+_{i+j}.
\]

This proves necessity. The same identity proves sufficiency. \(\square\)

Thus a rank-\(s\) seam is correctly credited at \(q=1\) to rank offset
\(t=s\). Fixed-depth grading is not exact once non-Johnson seams are
allowed.

There is nevertheless an exact rowwise signature defect identity. For
\(B\subseteq\{x,y\}\), let \(c_{q,B}\) be the number of
length-\((q+1)\) windows whose union has signature exactly \(B\), let
\(\kappa_{q,B}\) count those windows whose union rank is not \(R+q\),
and let \(E_{q,B}\) be the collision excess among the remaining
correct-rank windows. Then the number of missing targets is

\[
\boxed{
 H_{q,B}=\binom{2r-1}{R+q-|B|}
 -c_{q,B}+\kappa_{q,B}+E_{q,B}.}
\tag{6.1b}
\]

Indeed, \(c_{q,B}-\kappa_{q,B}\) is the number of correct-rank
occurrences, and subtracting \(E_{q,B}\) gives their distinct support.

The raw signature counts are determined exactly by sector runs:

\[
 c_{q,\varnothing}=\sum_{U\text{-runs}}(\ell-q)_+,
\tag{6.1c}
\]

\[
 c_{q,\{x\}}
 =\sum_{U/X\text{-runs}}(\ell-q)_+-c_{q,\varnothing},
\tag{6.1d}
\]

with the analogous formula for \(\{y\}\); the \(\{x,y\}\) count is
the complement among all \(W^+-q\) windows. Thus residence, which controls
internal one-runs, controls neither \(\kappa\) nor \(E\). When every edge
of a window is Johnson, correct rank means that every step inserts a
coordinate not already present in the running union, equivalently that no
coordinate makes a \(1\!-\!0\!-\!1\) return in that window. A
non-Johnson seam may overshoot the row's target rank and is then charged in
\(\kappa\), while still being useful at another rank through (US*). Global
rank-\(t\) holes are obtained from the union across \(q\), not by summing
the rowwise defects (6.1b).

For a bit set \(B\subseteq\{x,y\}\), define

\[
 \mathcal U_{q,B}(T^+)=
 \left\{
  \left(\bigcup_{j=0}^{q}T^+_{i+j}\right)\setminus\{x,y\}:
  \left(\bigcup_{j=0}^{q}T^+_{i+j}\right)\cap\{x,y\}=B,
  \left|\bigcup_{j=0}^{q}T^+_{i+j}\right|=R+q
 \right\}.
\tag{6.2}
\]

The stronger **graded** upper-shadow condition is

\[
\boxed{
 \mathcal U_{q,B}(T^+)
 =\binom{[2r-1]}{R+q-|B|}}
\tag{GUS}
\]

for every nonempty target layer, every \(q\ge1\), and every \(B\). It
implies (US*) but is not necessary when seams may change rank depth. By
(2.3), these projections have old signed depth \(q+1-|B|\). Thus an old
all-depth shadow carrier supplies the correct label families, but (6.1)
shows that it does not guarantee their survival after the pieces are
reordered.

Condition (US*) permits non-Johnson seams and credits them at the rank
dictated by Lemma 5.1. Such a seam is harmless only when every target lost
at its cuts has a retained or new cross-depth witness.

### Corollary 6.2 (long arms forced by graded upper support)

For \(r\ge3\), the stronger graded condition (GUS) forces

\[
 \max |U\text{-block}|\ge r-1,
\tag{6.3}
\]

\[
 \max |U/X\text{-run}|\ge r,
 \qquad
 \max |U/Y\text{-run}|\ge r,
\tag{6.4}
\]

and a correct-rank signature-\(\{x,y\}\) window of length \(r+1\).

#### Proof

At depth \(r-2\), the unique empty-signature target is the old full ground
set \([2r-1]\). Its length-\((r-1)\) witness lies wholly in \(U\), proving
(6.3). At depth \(r-1\), the targets
\([2r-1]\cup\{x\}\) and \([2r-1]\cup\{y\}\) require length-\(r\)
windows in \(U/X\) and \(U/Y\), respectively. At depth \(r\), the full
new ground set requires the last asserted window. \(\square\)

The Catalan mean \((W-b)/b=(r-1)/2\) is therefore not an admissible
uniform \(U\)-block length for the graded full upper tower. The deadline-safe
skeleton of Theorem 2.1 cannot be used unchanged when its forced nonempty
\(U\)-blocks are all shorter than \(r-1\). A braid required to satisfy
(GUS) must reduce or redistribute the \(U\)-blocks, compensate the lower-q1
ledger through other seams, and create a genuinely long \(U\)-arm.

### Proposition 6.3 (protected Catalan-selector obstruction)

Assume the old carrier is cyclic and write (with indices understood
cyclically)

\[
 V_i=T_i\cup T_{i+1}.
\]

In the strict inherited-edge \(U\)-lift, choose one occurrence of every
old rank-\((r+1)\) colour and let \(I\) be the selected index set. Then

\[
 |I|=W-b,\qquad |I^c|=b.
\tag{6.5}
\]

The graded empty-signature shore at depth \(q\) is complete if and only if

\[
\boxed{
 \forall Z\in\binom{[2r-1]}{r+1+q}\ \exists i:
 \bigcup_{j=0}^{q+1}T_{i+j}=Z
 \quad\text{and}\quad
 \{i,\ldots,i+q\}\subseteq I.}
\tag{6.6}
\]

#### Proof

An empty-signature window lies wholly in a \(U\)-block, and

\[
 \bigcup_{j=0}^{q}V_{i+j}
 =\bigcup_{j=0}^{q+1}T_{i+j}.
\]

It survives the one-occurrence-per-colour selection exactly when all indices
\(i,\ldots,i+q\) were retained. \(\square\)

A later linear cut must, in addition, leave at least one such witness for
every target without using a deleted wraparound window.

Old upper completeness gives only the first clause of (6.6). It does not
give a Catalan complement \(I^c\) which avoids hitting every occurrence
interval of every deeper target. If two uniquely witnessed deeper targets
force two different occurrences of the same immediate colour, no such
selector exists. Cross-sector seams cannot repair this empty-signature loss,
because every seam leaving \(U\) has nonempty signature. Arbitrary new
\(UU\) rethreading is outside Proposition 6.3, but must then be verified
directly through the rowwise ledger (6.1b) and the cross-depth condition
(US*).

## 7. Lower compiler: exact multirow PCSH and its Hall specialization

Assume residence, and let the maximal depth-\(d^+\) envelope be

\[
 E_p=
 \bigcap_{\max(0,p-d^+)\le i\le\min(W^+-1,p)}T^+_i,
 \qquad0\le p<W^++d^+.
\tag{7.1}
\]

The uniform compiler must use all \(d^+\) rows below the middle. Partition
the complete lower ideal into row families

\[
 \mathcal L_0\sqcup\cdots\sqcup\mathcal L_{d^+-1}
 =\{S\subseteq[2r+1]:1\le|S|<R\}.
\tag{7.2}
\]

For every \(S\in\mathcal L_t\), choose a start
\(0\le\phi_t(S)<W^++d^+-t\), injectively within row \(t\), and prescribe
the pin

\[
 (D^tA)_{\phi_t(S)}=S.
\tag{7.3}
\]

Add all central pins, all chosen seam pins, and the at most two boundary
flags. For a coordinate \(z\), define

\[
 Q_z=[0,W^++d^+-1]\setminus
 \bigcup_{(t,i,S):z\notin S}[i,i+t],
\tag{7.4}
\]

and put \(U_p=\{z:p\in Q_z\}\).

### Proposition 7.1 (exact multirow pin criterion)

The prescribed row assignment has a nonzero realization if and only if

\[
 z\in S\quad\Longrightarrow\quad[i,i+t]\cap Q_z\ne\varnothing
\tag{7.5}
\]

for every pin \((t,i,S)\), and

\[
 U_p\ne\varnothing\qquad(0\le p<W^++d^+).
\tag{7.6}
\]

When these conditions hold, the coordinatewise maximal word
\(A_p=U_p\) realizes every pin.

#### Proof

A pin excluding \(z\) forbids \(z\) throughout its physical interval,
which gives (7.4). A pin containing \(z\) requires one surviving occurrence
in that interval, which is (7.5). These conditions are necessary. Conversely,
putting every allowed coordinate into \(A_p\) excludes every negative
coordinate and hits every positive coordinate in every pin. Condition (7.6)
makes all entries nonzero. \(\square\)

Existence of the partition, starts, and one simultaneous coordinatewise core
in Proposition 7.1 is the exact **multirow PCSH** gate. Independent choices
for different rows have the wrong quantifier.

There is a useful but nonuniform specialization. After some intermediate
targets have been pinned, put every remaining target of rank at most
\(R-d^+\) literally in row zero. Choose a common pin-hitting core
\(C_p\subseteq U_p\) and define

\[
 S\sim p\quad\Longleftrightarrow\quad C_p\subseteq S\subseteq U_p.
\tag{7.7}
\]

Then the literal-low specialization is feasible exactly when

\[
\boxed{
 |\Gamma(\mathcal S)|\ge|\mathcal S|
 \quad\text{for every residual literal family }\mathcal S.}
\tag{LH\(_0\)}
\]

This is the selected-pin Hall compiler used in small dimensions. It is not a
uniform induction theorem: the literal-low target family can exceed the
\(W^++d^+\) base positions. The uniform condition is Proposition 7.1, with
targets distributed across all lower rows.

Neither the four scalar counts in (2.2) nor the deadline slack (1.7) implies
multirow PCSH. Old row assignments also do not tensor: the four target
sectors share one physical word, and braid seams change the common allowed
sets (7.4).

After the immediate lower rank is reserved, the four residual demand sizes
are exactly

\[
\boxed{
\begin{aligned}
 D_U&=\Lambda,\\
 D_X=D_Y&=\Lambda-W+1,\\
 D_A&=\Lambda-W-(W-b)+1.
\end{aligned}}
\tag{7.8}
\]

Their sum is \(\Lambda^+-W^+\). These are necessary batch totals, not
separate Hall problems: all four use one physical compiler.

### Proposition 7.2 (the same-depth full-family capacity trial is closed)

Four disjoint old depth-\(d\) lower triangles have

\[
 4(dW+T_d)
\]

lower cells. A same-depth fused child triangle has

\[
 d(4W-b)+T_d.
\]

Thus fusion removes exactly

\[
 db+3T_d
\tag{7.9}
\]

cell slots, while the child has three more lower targets than four old
lower ideals. Hence the full-family capacity condition is exactly

\[
 4\sigma\ge db+3T_d+3,
\]

which is the deadline criterion (1.6).

#### Proof

Subtract the two displayed cell counts and use
\(\Lambda^+=4\Lambda+3\). \(\square\)

Thus the same-depth scalar trial is completely decided by (1.6). If the
deadline rises, the applicable capacity is the second slack line of (1.7).
The unresolved issue is where the lost neighbourhood lies.

### Proposition 7.3 (exact proper-subset fusion inequality for a fixed bank)

Let \(D\) be a target family, and fix an unfused compiler bank
\(G_0=(D,C_0)\) and one common core. Call the bank and a proposed fusion
**common-core-compatible** when, for every \(X\subseteq D\), its actual
fused neighbourhood is

\[
 N_{\rm fus}(X)=
 \bigl(\pi(N_0(X))\setminus\{\bot\}\bigr)\cup N_J(X).
\tag{7.10a}
\]

Here

- \(\pi:C_0\to C\cup\{\bot\}\) is the physical fusion map, permitting
  deletion and coalescence;
- \(J\) is the set of genuinely new seam resources; and
- \(N_0(X)\) and \(N_J(X)\) are the old-bank and new-seam neighbourhoods
  of \(X\subseteq D\).

Define

\[
 s_0(X)=|N_0(X)|-|X|,
\]

\[
 \kappa_\pi(X)=|N_0(X)|-
 \left|\pi(N_0(X))\setminus\{\bot\}\right|,
\]

and

\[
 \gamma_\pi(X)=
 \left|N_J(X)\setminus
 \bigl(\pi(N_0(X))\setminus\{\bot\}\bigr)\right|.
\]

Then the fused graph satisfies Hall if and only if

\[
\boxed{
 \kappa_\pi(X)-\gamma_\pi(X)\le s_0(X)
 \qquad\text{for every }X\subseteq D.}
\tag{7.10}
\]

#### Proof

By common-core compatibility,

\[
 |N_{\rm fus}(X)|
 =|N_0(X)|-\kappa_\pi(X)+\gamma_\pi(X).
\]

The inequality \(|N_{\rm fus}(X)|\ge|X|\) is exactly (7.10). \(\square\)

Proposition 7.3 is an exact statement about the displayed bipartite graph.
For a physical multirow compiler it is necessary, but it is sufficient only
when the bank is independently programmable in the following strong sense:
every selected matching yields one simultaneously feasible family of row
pins with the advertised common core. Overlapping derivative intervals need
not have this property. In the general case Proposition 7.1 remains the
authoritative physical condition.

The cell-count relaxation of the full-set case is Proposition 7.2; an actual
full-set neighbourhood can of course be smaller than the raw triangle.
Proper subsets retain the named losses and cannot be recovered from that
scalar inequality. Moreover, (7.10) is useful only after all parent rows and
seam pins have been certified against one common coordinatewise
interval-hitting core; independent rowwise cores have the wrong quantifier.

## 8. The exact conditional induction theorem

### Theorem 8.1 (seam-relaxed four-sector induction)

Let \(k=2r-1\) with \(r\ge2\). Suppose an old carrier \(P\) satisfies the hypotheses of
Theorem 3.1 and has immediate upper support equal to the full
rank-\((r+1)\) layer. Form the new middle deck (2.1), and retain the exact
Catalan \(A\)-forest from Theorem 3.1, meaning that its selected edges remain
consecutive in the new order.

Assume there is an ordering \(T^+\) of this deck, allowing seams of arbitrary
rank distance subject to the following conditions:

1. **Residence:** Lemma 5.2 holds at the exact depth \(d^+\) given by
   Theorem 1.1.
2. **Upper support:** the exact cross-depth condition (US*) holds.
3. **Lower compiler:** the complete lower ideal has a multirow assignment
   (7.2)--(7.3), together with all central, seam, and boundary pins,
   satisfying the simultaneous pin conditions (7.5) and the nonzero
   condition (7.6).

Then there is a nonzero literal word of length

\[
 W^++d^+=B(2r+1)
\]

covering every nonempty subset of \([2r+1]\). Consequently

\[
 \boxed{\nu(2r+1)=B(2r+1).}
\]

#### Proof

Residence makes (7.1) a depth-\(d^+\) factor of \(T^+\). Proposition 7.1
gives a nonzero word \(A\) of length \(W^++d^+\) realizing every lower,
seam, boundary, and central pin. Thus it covers the complete lower ideal,
and its central row enumerates the entire rank-\(R\) layer.

For every \(q\ge1\),

\[
 D^{d^++q}A=D^qT^+.
\]

Condition (US*) therefore covers every upper layer. The word is universal.
The monotone-deadline theorem supplies the matching lower bound. \(\square\)

This theorem is stronger than a Johnson-only braid theorem: non-Johnson
seam distances may be used to place missing depth-two or deeper compiler
roots, provided the q1 boundary capacity and every condition of the theorem
hold. This does not license an unrestricted number of deficient seams.

## 9. Why old optimality alone does not trigger Theorem 8.1

There are four logically separate failures.

1. **An optimal word need not expose a carrier.** For \(k=4\), the optimal
   word
   \[
   (10,9,5,1,2,4,8)
   \]
   has length \(B(4)=7\), but its first central candidate
   \(10\cup9=11\) has rank three rather than the middle rank two. Thus its
   depth-one row is not a middle permutation. Equality in the scalar lower
   bound does not produce the input of Theorem 3.1.
2. **A carrier need not have the required old shadows.** One-hole immediate
   lower rainbowness does not by itself imply the completed second lower
   shadow or the all-depth upper supports.
3. **Old residence is insufficient even without a deadline rise.** Passing
   to the chronological intersection strand shortens an old run by one, so
   Theorem 5.3 must already cut old runs of length at most \(d^++1\). A
   deadline rise additionally strengthens the inherited \(X/Y\) port
   requirements.
4. **Shadows and residence do not imply multirow PCSH.** One must allocate
   all lower targets across derivative rows with one common coordinatewise
   interval-hitting core. Target counts, marginal shadow coverage, and
   separate sector compilers do not provide that quantifier.

Hence no induction from the bare equation \(\nu(k)=B(k)\) is valid.

## 10. Precise remaining theorem

Under the old-carrier hypotheses of Theorem 3.1, the label supply and the
both-new Catalan forest are closed. The smallest remaining statement within
this inherited four-sector architecture is:

> **Four-sector routing theorem (unproved).** For every old carrier in the
> induction class, the deck consisting of its completed lower row, two
> middle copies, and its upper support admits one seam-relaxed ordering
> with all of the following simultaneous properties:
>
> 1. on the strict inherited \(A\)-shore, the retained \(W-b\) native
>    edges are exactly the \(AA\) adjacencies, select one witness of every
>    old depth-two lower colour, and their complementary \(b-1\) deleted
>    edges hit the short-run family of Theorem 5.3; alternatively, a
>    rethreaded \(A\)-shore covers the same colours and its full deleted
>    native-edge set is a transversal of that family;
> 2. all exposed ports satisfy Lemma 5.2 at the exact new deadline;
> 3. when the old carrier is cyclic, either the Catalan immediate-upper
>    occurrence selector satisfies (6.6) in its strict inherited graded
>    shore and the whole braid satisfies the exact cross-depth condition
>    (US*), or an explicitly rethreaded \(U\)-shore is verified directly by
>    (6.1b) and (US*); for a linear old carrier only the latter formulation
>    is asserted;
> 4. the complete lower ideal has one multirow assignment satisfying
>    Proposition 7.1; for any implementation through a fixed fusion bank,
>    its proper-subset losses satisfy (7.10); and
> 5. at most two immediate lower holes are placed on compatible endpoint
>    flags.

The word “simultaneously” is essential. Separate residence routing, separate
upper witness replacement, and separate lower Hall matchings can select
incompatible seams.

The three smallest lane-specific obstructions are therefore now explicit:

\[
 \tau_{d^++1}(P)>b-1
 \tag{R-obstruction}
\]

closes the native chronological \(A\)-batching residence route;

\[
 \text{no Catalan occurrence selector satisfying (6.6)}
 \tag{U-obstruction}
\]

closes the strict inherited graded \(U\)-shore when the old carrier is
cyclic, though not a linear or arbitrarily rethreaded \(UU\)-shore; and

\[
 \exists X\subseteq D:\quad
 \kappa_\pi(X)-\gamma_\pi(X)>s_0(X)
 \tag{H-obstruction}
\]

closes a proposed physical lower fusion. The first two are
architecture-specific; the last is exactly Hall for the chosen common-core
bank.

Theorem 1.1 also shows the precise extra burden at a deadline jump. The
Catalan identity removes \(b=C_r\) central positions, but if

\[
 4\sigma<db+3T_d+3,
\]

the old depth has insufficient scalar capacity and the lift must operate at
depth \(d+1\). Even when the reverse inequality holds, (US*) and multirow
PCSH remain genuine labelled conditions. This is the exact
proved/conditional boundary of the \(k\mapsto k+2\) lane.
