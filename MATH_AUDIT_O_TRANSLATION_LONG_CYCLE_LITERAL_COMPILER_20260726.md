# Translation-invariant long odd-graph cycles: exact literal compiler and the bad-window boundary

Date: 2026-07-26

Method: pure mathematics only.  No finite search, computation, solver, or
web input is used.

## 0. Verdict

Let

\[
                 n=2m+1,\qquad
                 W=\binom{2m+1}{m}.
\tag{0.1}
\]

An exact directed cycle cover of the odd graph \(KG(2m+1,m)\), of
arbitrary cycle lengths, **does** plug into the established factor-blind
constant-one compiler.  Shortest \((2m+1)\)-cycles are not required.
There are, however, three separate hypotheses:

1. the every-second Johnson traversals must have the literal delay
   property through the chosen depth;
2. the number of resulting alternating middle-level components must be
   \(o(W/H)\); and
3. the actual lower-shadow holes through the window must total \(o(W)\).

The third condition is not implied by the first two.  Local
return-freeness proves that an occurrence is legal and has the right
rank; it does not prevent different occurrences from colliding on the
same target.

There is also a useful correction to the preliminary long-cycle note.
The upper traces are not missing.  For every directed odd-graph cycle,
the upper depth-\(q\) trace of one parity traversal is the complement of
the lower depth-\(q\) trace of the opposite parity traversal.  Thus

\[
                 \mu_q^+(U)=\mu_q^-(U^c),
                 \qquad M_q^+=M_q^-.
\tag{0.2}
\]

Consequently a one-sided lower-shadow theorem is enough.

The exact full-depth bound proved below is

\[
 \boxed{
 \nu(2m+1)
 \le W+(2d+1)K
       +2\sum_{q=1}^{d}M_q^-
       +2L_m(m-d-1),}
\tag{0.3}
\]

where \(K\) is the number of alternating components, all components
satisfy the geodesic condition \(G_d\) and positive-dwell condition
\(P_d\), and \(M_q^-\) is the actual number of missing lower
rank-\((m-q)\) targets.

Ordinary cyclic \(H\)-geodesicity implies only \(P_{H-1}\), not
\(P_H\).  With that weaker input the safe exact bound is

\[
 \boxed{
 \nu(2m+1)
 \le W+(2H-1)K
       +2\sum_{q=1}^{H-1}M_q^-
       +2L_m(m-H).}
\tag{0.4}
\]

The one-depth retreat is asymptotically invisible when
\(H/\sqrt m\to\infty\).

The phrase “all but \(o(W)\) windows are return-free” is sufficient only
if “windows” means the aggregate collection of **literal signed
occurrence slots at every depth** whose prescribed atom identities fail.
If it means merely \(o(W)\) bad owners, short runs, or rooted maximal
\(H\)-tests, it is not sufficient without a stronger rate.  One bad
maximal test can invalidate \(\Theta(H)\) middle-owner atom identities,
and a support-blind cut costs exactly \((H+1)^2\) central occurrences.

Finally, the existence of a proper \(p\)-edge-colouring of the projected
arc multigraph does not enforce any of the three conditions above.  They
are higher-order constraints on consecutive edges, cycle voltage, global
cycle structure, and trace colours.  A constrained colour class with
these properties would prove the desired prime-subsequence input, but it
does not follow from regularity or Koenig edge-colouring alone.

## 1. From a directed odd-graph cover to an exact alternating cover

Let \(\Omega\) be a set of size \(2m+1\), and let

\[
 \sigma:\binom{\Omega}{m}\longrightarrow\binom{\Omega}{m}
\tag{1.1}
\]

be a permutation satisfying

\[
                         A\cap\sigma(A)=\varnothing
                         \qquad(A\in\binom{\Omega}{m}).
\tag{1.2}
\]

Thus the directed cycles of \(\sigma\) are a directed cycle cover of the
odd graph.  Fix one cycle

\[
                         A_0,A_1,\ldots,A_{\ell-1}.
\tag{1.3}
\]

Indices in this section are cyclic.

If \(\ell\) is odd, define one alternating component by

\[
 X_j=A_{2j},\qquad Y_j=\Omega\setminus A_{2j+1}
                 \qquad(j\in\mathbb Z/\ell\mathbb Z).
\tag{1.4}
\]

If \(\ell\) is even, define two components, for \(r=0,1\), by

\[
 X_j^{(r)}=A_{r+2j},\qquad
 Y_j^{(r)}=\Omega\setminus A_{r+2j+1}
                 \qquad(j\in\mathbb Z/(\ell/2)\mathbb Z).
\tag{1.5}
\]

### Lemma 1.1 (exact bipartite double cover)

If \(\ell\ne2\), every component in (1.4)--(1.5) satisfies

\[
                         Y_j=X_j\cup X_{j+1}.
\tag{1.6}
\]

Over all directed cycles, the \(X\)-occurrences partition rank \(m\),
and the \(Y\)-occurrences partition rank \(m+1\).

#### Proof

Both \(A_i\) and \(A_{i+2}\) are contained in
\(\Omega\setminus A_{i+1}\), which has size \(m+1\).  If they were
equal, simplicity of the permutation cycle would force \(\ell=2\).
Otherwise they are distinct \(m\)-subsets of the same \((m+1)\)-set, so
their union is that whole set.  This proves (1.6).

When \(\ell\) is odd, multiplication by two permutes the cycle indices,
so (1.4) uses every \(A_i\) once on each shore, with complementation on
the upper shore.  When \(\ell\) is even, the two choices of \(r\) split
the even and odd indices and again use every \(A_i\) once on each shore.
Summing over the cycles proves exactness. \(\square\)

A directed two-cycle is an immediate backtrack.  It produces two
degenerate one-owner alternating components for which (1.6) fails.  Such
owners must be placed in the exceptional ledger.  In particular, any
positive-depth return-free hypothesis excludes two-cycles automatically.

For later comparison with the quotient voltage labels, define the unique
omitted point on an odd-graph arc by

\[
                         u_i=\Omega\setminus(A_i\cup A_{i+1}).
\tag{1.7}
\]

Away from an immediate backtrack,

\[
 \boxed{
 A_{i+2}=\bigl(A_i\setminus\{u_{i+1}\}\bigr)\cup\{u_i\}.}
\tag{1.8}
\]

Indeed, both \(A_i\) and \(A_{i+2}\) are \(m\)-subsets of
\(\Omega\setminus A_{i+1}=A_i\cup\{u_i\}\); the point deleted in
passing to \(A_{i+2}\) is exactly \(u_{i+1}\).  Thus an every-second
transition deletes \(u_{i+1}\) and inserts \(u_i\).  Pairwise
distinctness of the relevant consecutive omitted labels is a convenient
sufficient return-free condition, although the exact two-queue residence
condition is weaker.

If the directed odd-graph factor has \(c_{\rm odd}\) odd cycles and
\(c_{\rm even}\) even cycles, excluding the exceptional two-cycles, the
number of alternating components is exactly

\[
                         K=c_{\rm odd}+2c_{\rm even}
                         \le2c(\sigma).
\tag{1.9}
\]

## 2. The upper shore is exactly the complementary lower shore

For a component in (1.4) or (1.5), define

\[
 L_{j,q}=\bigcap_{t=0}^{q}X_{j+t},
 \qquad
 U_{j,q}=\bigcup_{t=0}^{q+1}X_{j+t}.
\tag{2.1}
\]

The intended ranks are \(m-q\) and \(m+1+q\), respectively.  Let the
opposite-parity traversal be

\[
                         X'_j=A_{r+2j+1}.
\tag{2.2}
\]

For an even original cycle it is the other component in (1.5).  For an
odd original cycle it is a cyclic reindexing of the same component,
because two is invertible modulo \(\ell\).

### Lemma 2.1 (exact trace complement)

For every \(q\ge0\),

\[
 \boxed{
 U_{j,q}^{,c}=\bigcap_{t=0}^{q}X'_{j+t}.}
\tag{2.3}
\]

Consequently, over the complete directed factor,

\[
 \boxed{
 \mu_q^+(U)=\mu_q^-(U^c),\qquad
 M_q^+=M_q^-.}
\tag{2.4}
\]

The same equality holds for every overload, floor-distance, or hole
functional invariant under complementation.

#### Proof

By (1.6),

\[
                         (X_{j+t}\cup X_{j+t+1})^c=X'_{j+t}.
\tag{2.5}
\]

The union of the \(q+1\) adjacent pairs on the left of (2.5) is exactly
\(X_j\cup\cdots\cup X_{j+q+1}=U_{j,q}\).  Taking complements proves
(2.3).  Opposite parity is a bijection on all rooted occurrence slots,
and complementation is a bijection from rank \(m-q\) to rank
\(m+1+q\).  This proves (2.4). \(\square\)

This identity is special to the odd-graph double cover.  It repairs the
apparent upper-interface gap in the preliminary long-cycle formulation.

## 3. Exact literal factor for one arbitrary-length component

Let

\[
                         C=(X_i)_{i\in\mathbb Z/\lambda\mathbb Z}
\tag{3.1}
\]

be one alternating component.  For an integer \(d<m\), use the following
two distinct conditions.

* \(G_d\): every cyclic segment of at most \(d\) Johnson transitions is
  geodesic.  Equivalently,

  \[
  |L_{i,q}|=m-q\qquad(0\le q\le d).
  \tag{3.2}
  \]

  By Lemma 2.1 on the opposite parity, this also gives
  \(|U_{i,q}|=m+1+q\).

* \(P_d\): in the cyclic binary state row of every ground coordinate,
  every nonconstant positive run has at least \(d+1\) states.

Define the cyclic atoms

\[
                         B_j=\bigcap_{s=0}^{d}X_{j-s}.
\tag{3.3}
\]

### Lemma 3.1 (odd long-cycle delay identities)

Under \(P_d\), for \(0\le q\le d\),

\[
 \boxed{
 X_i=\bigcup_{j=i}^{i+d}B_j,}
\tag{3.4}
\]

\[
 \boxed{
 L_{i,q}=\bigcup_{j=i+q}^{i+d}B_j,}
\tag{3.5}
\]

and

\[
 \boxed{
 U_{i,q}=\bigcup_{j=i}^{i+q+d+1}B_j.}
\tag{3.6}
\]

#### Proof

Fix a coordinate and inspect its binary cyclic row.  If it is present in
\(X_i\), the positive run containing \(i\) has at least \(d+1\) states.
It therefore contains a block of \(d+1\) one-states containing \(i\),
whose right endpoint lies in \([i,i+d]\).  This proves (3.4)
coordinatewise.

If the coordinate is present throughout \([i,i+q]\), the same positive
run contains a block of \(d+1\) one-states containing that interval; its
right endpoint can be chosen in \([i+q,i+d]\).  This proves (3.5).

Finally, union (3.4) for \(X_i,\ldots,X_{i+q+1}\).  The union of their
atom-index intervals is \([i,i+q+d+1]\), proving (3.6). \(\square\)

Emit the linear literal word

\[
 \boxed{
 B_0,B_1,\ldots,B_{\lambda-1},B_0,B_1,\ldots,B_{2d}.}
\tag{3.7}
\]

It has exact length

\[
                              \lambda+2d+1.
\tag{3.8}
\]

The copied prefix linearizes every interval in (3.4)--(3.6).  In
particular the upper depth-\(d\) witness contains \(2d+2\) atoms and
requires the final copied atom \(B_{2d}\).  Empty atoms, if any in a
defective application, may be deleted after witnesses are fixed; deleting
empty letters preserves contiguity and every union.

Ordinary \(G_d\) does not imply \(P_d\).  It implies only

\[
                              G_d\Longrightarrow P_{d-1}.
\tag{3.9}
\]

A convenient sufficient input for the full-depth word is \(G_{d+1}\),
or directly the weaker exact condition \(G_d+P_d\).

## 4. Exact global compiler and all constants

For completeness, define the established product-SCD tail length by

\[
 A_m(a)=\binom ma-\binom m{a-1},
\tag{4.1}
\]

\[
 w_m(a)=
 \begin{cases}
 m,&a=0,\\
 m-2a+1,&a>0,
 \end{cases}
\tag{4.2}
\]

and

\[
 C_m(t)=
 \begin{cases}
 0,&t<0,\\
 \displaystyle\binom m{\min(t,\lfloor m/2\rfloor)},&t\ge0.
 \end{cases}
\tag{4.3}
\]

Then

\[
 \boxed{
 L_m(r)=2\sum_{a=0}^{\lfloor m/2\rfloor}
 A_m(a)w_m(a)C_m(r-a).}
\tag{4.4}
\]

One odd-dimensional exterior word has length \(2L_m(m-d-1)\) and covers
exactly the ranks outside

\[
                         [m-d,m+d+1].
\tag{4.5}
\]

There is an absolute constant \(C_0\) such that

\[
 \frac{L_m(m-d-1)}{\binom{2m}{m}}
 \le C_0\exp\!\left(-\frac{d^2}{8m}\right).
\tag{4.6}
\]

### Theorem 4.1 (arbitrary-length directed odd-factor compiler)

Let a directed odd-graph cycle factor have no two-cycles, and let its
alternating double cover have \(K\) components.  Assume every component
satisfies \(G_d+P_d\).  Let \(M_q^-\) be the number of rank-\((m-q)\)
targets absent from all lower traces \(L_{i,q}\).  Then (0.3) holds.

#### Proof

The alternating components contain exactly \(W\) lower owners.  Summing
(3.8) over them gives a central literal word of length

\[
                              W+(2d+1)K.
\tag{4.7}
\]

It covers every occurrence supplied by the factor, on both signs, by
Lemma 3.1.  Rank \(m\) and rank \(m+1\) are covered exactly by Lemma 1.1.
At positive depth, Lemma 2.1 says that the upper and lower missing-target
counts are equal.  Append each missing lower and upper target once, at
total cost

\[
                              2\sum_{q=1}^dM_q^-.
\tag{4.8}
\]

Append the single odd product-SCD exterior word of length
\(2L_m(m-d-1)\).  Every witness lies wholly within one displayed block,
so concatenation creates no seam charge. \(\square\)

### Corollary 4.2 (constant-one plug-in)

If

\[
 \frac d{\sqrt m}\longrightarrow\infty,
 \qquad K=o(W/d),
 \qquad \sum_{q=1}^{d}M_q^-=o(W),
\tag{4.9}
\]

then

\[
                              \nu(2m+1)=(1+o(1))W.
\tag{4.10}
\]

#### Proof

The component collar in (0.3) is \(o(W)\), and (4.8) is \(o(W)\).
Equations (4.6) and

\[
 \binom{2m+1}{m}=\frac{2m+1}{m+1}\binom{2m}{m}
\tag{4.11}
\]

make the exterior word \(o(W)\).  The largest-layer endpoint injection
gives the matching lower bound \(\nu(2m+1)\ge W\). \(\square\)

### Corollary 4.3 (exceptional directed two-cycles)

Suppose \(r_2\) physical odd-graph owners lie on directed two-cycles.
Discard those two-cycles and apply Theorem 4.1 to all remaining cycles.
If their alternating double cover has \(K\) components and is
\(G_d+P_d\), then

\[
 \boxed{
 \nu(2m+1)
 \le W+r_2+(2d+1)K
      +2\sum_{q=1}^{d}M_{q,\mathrm{ret}}^-
      +2L_m(m-d-1).}
\tag{4.12}
\]

Indeed, the retained atom words have base mass \(W-r_2\).  Appending the
missing \(r_2\) lower-middle owners and their \(r_2\) complementary
upper-middle owners changes that base to \(W+r_2\).  Every positive-depth
loss is already counted by the actual retained lower holes and their
complementary upper holes.  Thus \(r_2=o(W)\) is harmless; immediate
backtracks need not be forbidden absolutely.

If only ordinary \(G_H\) is known, apply the theorem with \(d=H-1\).
This proves (0.4), and (4.6) becomes

\[
 \frac{L_m(m-H)}{\binom{2m}{m}}
 \le C_0\exp\!\left(-\frac{(H-1)^2}{8m}\right).
\tag{4.13}
\]

There is no additional parity loss.  The construction is already a
direct word in odd dimension.  The factor two in the last term of (0.3)
is exactly the trimmed odd lift of the **single** two-tail product-SCD
word.  It is not a second central copy.  Transfer from a dense prime odd
subsequence to all dimensions is a separate, already established theorem;
no reverse odd-to-even trimming is used here.

## 5. What “bad windows” must mean

The cleanest defective formulation keeps the cyclic atom word (3.7).
For every rooted signed slot, call the slot **literal-valid** if its
prescribed interval in (3.4), (3.5), or (3.6) equals the intended trace
and that trace has the intended rank.  Let

\[
 \mathcal B_d^{\rm lit}
 =\#\{\text{literal-invalid signed occurrence slots at depths }0,\ldots,d\}.
\tag{5.1}
\]

Let \(M_q^{-,\rm geom}\) count lower targets absent even before invalid
occurrences are discarded, among all geometrically rank-correct traces.
Then the number of central targets missing from the literal-valid slots is
at most

\[
 2\sum_{q=1}^{d}M_q^{-,\rm geom}
 +\mathcal B_d^{\rm lit},
\tag{5.2}
\]

plus any explicitly exceptional rank-\(m\) or rank-\((m+1)\) owners such
as directed two-cycles.

Indeed, every newly missing target which was geometrically present must
lose all its occurrences.  Choose one lost occurrence; distinct targets
choose distinct occurrence slots.  Thus the new holes inject into the
invalid slots.  Equation (5.2) follows, using complementary parity for
the geometric upper holes.

Therefore

\[
 \mathcal B_d^{\rm lit}=o(W),
 \qquad
 \sum_{q=1}^{d}M_q^{-,\rm geom}=o(W)
\tag{5.3}
\]

is a valid defective input to Theorem 4.1.  This is the precise sense in
which “return-free off \(o(W)\) windows” is accepted.

It is not equivalent to saying that only \(o(W)\) rooted maximal
return tests fail.

### Lemma 5.1 (one maximal return can spoil \(d\) owners)

Suppose the binary state row of one coordinate has a positive run of
exactly \(d\) states.  In the depth-\(d\) atom word, all \(d\) middle
identities (3.4) at those states fail for that coordinate.  Nevertheless,
the entering and leaving changes lie together in only one block of
\(d+1\) consecutive transitions of minimal such length.

#### Proof

No intersection of \(d+1\) consecutive states contains the coordinate
inside that positive run.  Hence none of the atoms available to any of
its \(d\) states contains the coordinate, although the middle state does.
The two boundary transitions are separated by exactly \(d\) transition
positions, so precisely the block beginning with the entering transition
contains both. \(\square\)

Thus an unweighted number \(b\) of bad maximal tests can create
\(\Theta(db)\) failed middle slots.  The claim \(b=o(W)\) alone has the
wrong scale.

There is a completely support-blind cut repair.  Suppose \(b\) cuts hit
all unsafe windows, leaving delay-\(d\) safe open paths, while \(K_0\)
components remain safe and cyclic.  A path with \(v\) lower states costs
\(v+d\) atoms; a cycle costs \(v+2d+1\).  Each cut loses one upper-middle
edge, \(q\) lower depth-\(q\) windows, and \(q+1\) upper depth-\(q\)
windows.  Hence its exact raw occurrence loss through depth \(d\) is

\[
 1+\sum_{q=1}^{d}(q+(q+1))=(d+1)^2.
\tag{5.4}
\]

If the pre-cut one-sided geometric hole count is
\(M^-_\bullet=\sum_{q=1}^{d}M_q^-\), the resulting literal bound is

\[
 \boxed{
 \nu(2m+1)
 \le W+d b+(2d+1)K_0
      +2M^-_\bullet+(d+1)^2b
      +2L_m(m-d-1).}
\tag{5.5}
\]

Accordingly, without direct knowledge of which targets survive, the cut
rate is

\[
                              b=o(W/d^2),
\tag{5.6}
\]

not merely \(b=o(W/d)\).  The latter rate controls the factor collar but
not the raw shadow loss.

## 6. Quotient matching components and the edge-colouring scope

Now specialize to prime \(p=2m+1\) and translation necklaces.  A perfect
matching of the projected \(p\)-regular bipartite arc multigraph is a
permutation of the \(T=W/p\) middle necklaces.  A quotient cycle of
length \(\ell\) and voltage \(v\) lifts to

\[
 \begin{cases}
 p\text{ physical cycles of length }\ell,&v=0,\\
 1\text{ physical cycle of length }p\ell,&v\ne0.
 \end{cases}
\tag{6.1}
\]

If \(c(M)\) is the number of quotient cycles, then

\[
 c(\sigma_M)\le p\,c(M),
 \qquad
 K(M)\le2p\,c(M).
\tag{6.2}
\]

Thus

\[
                              c(M)=o(T/H)
\tag{6.3}
\]

is a sufficient quotient condition for the physical collar
\((2H+1)K=o(W)\).  The sharper exact statistic is obtained from (6.1)
and the parity of each lifted physical cycle before applying (1.7).

The ordinary edge-colouring theorem proves only that each colour class is
a perfect matching.  It says nothing about:

1. consecutive pairs, hence immediate backtracks and Johnson moves;
2. repeated physical coordinates across \(H\) successive every-second
   moves, hence \(G_H\) or \(P_H\);
3. quotient cycle voltages and the physical component count in (6.1); or
4. the global lower trace colours and the holes \(M_q^-\).

All four are nonlinear in a single edge.  In particular they do not
average linearly over the \(p\) colour classes of an arbitrary
one-factorization.  Therefore the regularity/edge-colouring argument does
not prove that one colour has the required properties.  The remaining
positive theorem is a constrained quotient perfect matching (or a
simultaneous constrained one-factorization) satisfying

\[
 \boxed{
 K(M)=o(W/H),\qquad
 \mathcal B_{H-1}^{\rm lit}=o(W),\qquad
 \sum_{q=1}^{H-1}M_q^-(M)=o(W),}
\tag{6.4}
\]

for some \(H/\sqrt m\to\infty\).  Under (6.4), Theorem 4.1 with
\(d=H-1\) gives constant one on the prime subsequence.  No shortest-cycle
Catalan congruence or AP-loop condition remains.

## 7. Final proved and unproved boundary

Proved:

1. arbitrary directed odd-graph cycle covers give exact alternating
   middle-level covers after the parity double lift;
2. upper traces are exactly complements of opposite-parity lower traces;
3. arbitrary component lengths compile literally with exact collar
   \(2d+1\) per alternating component under \(G_d+P_d\);
4. ordinary \(G_H\) compiles safely through \(H-1\);
5. the exact word, tail, rank, seam, and parity ledger is (0.3)--(0.4);
6. aggregate literal-slot defect \(o(W)\) is acceptable, whereas an
   unweighted \(o(W)\) bad-owner or bad-maximal-window assertion is not;
   and
7. a support-blind cut loses exactly \((d+1)^2\) central occurrences.

Not proved:

1. that one perfect matching in the projected MSW arc multigraph satisfies
   (6.4);
2. any edge-colouring theorem controlling the consecutive-edge return
   constraints, voltages, and target colours simultaneously; or
3. the required one-sided lower-hole estimate for a growing Gaussian
   window.

Thus long cycles fully bypass the shortest-\(p\)-cycle Catalan
classification at the ownership level and are accepted by the
constant-one compiler.  The surviving gate is the constrained
chronological matching/coverage theorem, not a new literal OR interface.
