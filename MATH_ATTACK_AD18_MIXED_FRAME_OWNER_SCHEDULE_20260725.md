# AD18: integral owner-dependent recursive-frame scheduling for MFUP

Date: 2026-07-25

## 0. Verdict

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 H=\lceil A\sqrt m\rceil .
\tag{0.1}
\]

This note settles the owner and interface halves of the mixed-frame
useful-prefix problem exactly, but it does **not** prove the remaining
shadow-support estimate and hence does not prove coefficient one.

The positive theorem is as follows.  Start with any exact odd middle-wreath
factor on \([2m+1]\), cut it at one coordinate, and use the resulting exact
partition of \(\binom{[2m]}m\) into complementary Johnson geodesics.  For
every power of two \(\ell\) satisfying

\[
 2H<\ell\le m,\qquad H=o(\ell),
\tag{0.2}
\]

these paths admit an integral owner-dependent schedule of collared
\(F_\ell\)-segments such that

* the principal owners partition the middle layer exactly;
* every principal lower and upper flag through depth \(H\) is a literal
  interval in its phase word;
* the number \(C\) of pieces and the useful-prefix bridge excess obey

  \[
  C\le {W\over \ell-2H+1}+{W\over m+1},
  \qquad
  \operatorname{Br}\le2H(C-1)=o(W).
  \tag{0.3}
  \]

For the largest power of two \(\ell\le m\), eventually

\[
 C\le {3W\over m+1},\qquad
 \operatorname{Br}\le {6HW\over m+1}=O_A(W/\sqrt m)=o(W).
\tag{0.4}
\]

Thus exact owner integrality, mandatory frame mixing, recursive-cube
legality, collars, literal chronology, and interface toll are no longer
missing in this sublane.

The exact remaining quantity is the cross-geodesic interval-support defect.
For the path family \(\mathcal P\), define the signed support sets
\(S_q^-\) and \(S_q^+\) in Section 4.  The construction guarantees

\[
 \operatorname{Hol}_{\rm actual}
 \le
 \sum_{q=1}^H
 \bigl[(N_q-|S_q^-|)+(N_q-|S_q^+|)\bigr].
\tag{0.5}
\]

A precise capacitated-Hall sufficient condition is

\[
 \sum_{q=1}^H
 \bigl(\widehat\delta_q^-+\widehat\delta_q^+\bigr)=o(W).
\tag{0.6}
\]

It is unproved.  In particular, the lower depth-one term is already the
old first-shadow/MWB issue for the chosen exact wreath factor; it must not
be declared zero for an arbitrary factor.  The upper depth-one internal
unions, by contrast, do partition their layer exactly.

Two exact obstructions delimit the result.

1. Every individually relabelled \(F_\ell\)-cycle is just a core-lifted
   cyclic-interval necklace.  The full coordinate orbit of one native cycle
   already contains every such atom.  The recursive factorization gives an
   exact resolution of a whole orientation cube, but it gives no additional
   individual MFUP columns capable of forcing cross-component support.
2. Whenever \(3(\ell-1)\le m-2\), the middle-owner incidence matrix of
   genuine mixed-frame necklaces has the minimal non-TU minor

   \[
   \begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix},
   \qquad \det=2.
   \tag{0.7}
   \]

   When \(3(\ell-1)\le m-2\), a genuine local restricted-reservoir
   instance has additive LP integrality gap \(\ell\).  Hence the exact
   fractional orbit solution
   cannot be rounded by a hidden network-flow or total-unimodularity
   argument.  This local gap is not a global MFUP no-go because other
   cross-gadget necklaces may repair it.

All constructed selections, paths, collars, and words below are integral.
Fractional objects occur only in the explicitly labelled orbit comparison
of Section 2 and LP-gap audit of Section 7.

## 1. Cyclic-interval normal form for the recursive cycles

For a cyclic list of distinct symbols

\[
 z=(z_0,z_1,\ldots,z_{2\ell-1}),
\]

write

\[
 I_z(i,r)=\{z_i,z_{i+1},\ldots,z_{i+r-1}\},
\tag{1.1}
\]

with indices modulo \(2\ell\).

### Theorem 1.1 (exact cyclic-interval normal form)

Let

\[
 Z_0,Z_1,\ldots,Z_{2\ell-1}
\tag{1.2}
\]

be one embedded cycle of the recursive orientation-cube factor \(F_\ell\)
inside an \(\ell\)-frame.  Write

\[
 Z_{i+1}=Z_i-r_i+s_i.
\tag{1.3}
\]

After cyclic reindexing, its transition-pair word is

\[
 e_0,e_1,\ldots,e_{\ell-1},
 e_0,e_1,\ldots,e_{\ell-1}.
\tag{1.4}
\]

Orient \(e_i\) so that its first occurrence removes \(r_i\), and put

\[
 z_i=r_i,\qquad z_{i+\ell}=s_i
 \quad(0\le i<\ell).
\tag{1.5}
\]

If \(C\) is the fixed included core of the frame, then, for every cyclic
index \(i\),

\[
 \boxed{Z_i=C\cup I_z(i,\ell).}
\tag{1.6}
\]

Moreover, whenever \(0\le q\le\ell\),

\[
 \boxed{
 L_q(i):=\bigcap_{a=0}^q Z_{i+a}
       =C\cup I_z(i+q,\ell-q),}
\tag{1.7}
\]

and

\[
 \boxed{
 U_q(i):=\bigcup_{a=0}^q Z_{i-a}
       =C\cup I_z(i-q,\ell+q).}
\tag{1.8}
\]

Conversely, fix one native \(F_\ell\)-cycle.  Given disjoint sets
\(C,D\) of size \(m-\ell\) and any cyclic order \(z\) of the remaining
\(2\ell\) coordinates, one coordinate permutation maps that fixed native
cycle to the necklace in (1.6).  Consequently the full coordinate orbit of
one native cycle is already the family of all core-lifted cyclic-interval
necklaces.

#### Proof

At \(Z_0\), the chosen coordinate from pair \(e_i\) is \(r_i\): before
the first occurrence of \(e_i\), that pair has not been flipped.  Thus

\[
 Z_0=C\cup\{r_0,\ldots,r_{\ell-1}\}
     =C\cup I_z(0,\ell).
\]

Transition \(i\) replaces \(z_i\) by \(z_{i+\ell}\).  Hence it moves the
length-\(\ell\) cyclic interval one step, proving (1.6) by induction.
Intersecting the \(q+1\) intervals whose starts are
\(i,i+1,\ldots,i+q\) leaves the interval from \(i+q\) through
\(i+\ell-1\), which proves (1.7).  Taking the union of the intervals
starting at \(i,i-1,\ldots,i-q\) gives the interval from \(i-q\) through
\(i+\ell-1\), which proves (1.8).

For the converse, record in the fixed native cycle its fixed core, fixed
outside set, and the ordered removed and inserted coordinates in the first
half of its transition word.  Map those coordinates pointwise to

\[
 z_0,\ldots,z_{\ell-1},z_\ell,\ldots,z_{2\ell-1},
\]

and map the fixed core and outside coordinates bijectively to \(C,D\).
Equation (1.6) shows that this one permutation maps every cycle vertex, not
merely one transition.  \(\square\)

### Scope of Theorem 1.1

The cube-wide recursive theorem remains useful: it partitions every fixed
orientation cube into two-sided-rainbow cycles simultaneously.  Theorem
1.1 says something narrower and decisive for MFUP selection: once arbitrary
coordinate conjugation of each selected atom is allowed, the different
recursive cycles add indexed multiplicity but no new owner/shadow column.
Thus exponential internal cycle diversity cannot by itself settle an
integral cross-component selection problem.

## 2. Exact collared fractional reservoir

This section corrects a parameter-scope trap in the open-segment fractional
calculation.

Let \(R=2\ell\), and let \(B\) be one full recursive necklace with its
\(R\) distinct principal owners.  Give every principal owner its full
cyclic radius-\(H\) state: the last \(H\) predecessor transitions and the
first \(H\) successor transitions are a **conceptual collar**.  Cutting the
cycle at one point gives a legal phase with exact hard-start cost \(2H\).
The collars prescribe boundary flags; they are not separately owned middle
vertices.

### Proposition 2.1 (collared orbit cover)

Assume \(H\le\ell/2\).  Take all indexed coordinate relabellings
\(\sigma B\), \(\sigma\in S_{2m}\), and give each weight

\[
 x_\sigma={W\over (2m)!R}.
\tag{2.1}
\]

Then every middle owner has weighted degree exactly one, and every lower or
upper rank-\((m\mp q)\) target, \(1\le q\le H\), has weighted hit degree

\[
 \boxed{{W\over N_q}\ge1.}
\tag{2.2}
\]

The weighted hard-start mass is exactly

\[
 2H\sum_\sigma x_\sigma={2HW\over R}={HW\over\ell}=o(W)
\tag{2.3}
\]

whenever \(H=o(\ell)\).

#### Proof

The necklace has \(R\) distinct owners.  At every depth \(q\le H\),
Theorem 1.1 gives \(R\) distinct cyclic lower flags and \(R\) distinct
cyclic upper flags.  Transitivity of the symmetric group and double
counting therefore give indexed incidence degrees

\[
 {(2m)!R\over W}
 \quad\hbox{and}\quad
 {(2m)!R\over N_q}
\]

at a fixed owner and a fixed signed target, respectively.  Multiplication
by (2.1) proves (2.2) and the owner equality.  There are total fractional
atom mass \(W/R\), and each cut cyclic phase has exact hard-start cost
\(2H\), proving (2.3).  \(\square\)

Without collars, an open \(R\)-owner segment has only \(R-q\) guaranteed
internal \(q\)-windows, and its target load is

\[
 \left(1-{q\over R}\right){W\over N_q}.
\tag{2.4}
\]

At \(q=1\), (2.4) is at least one if and only if \(R\ge m+1\), because
\(N_1/W=m/(m+1)\).  Thus the uncollared formula cannot be imported into a
regime \(H\ll\ell=o(m)\).  Proposition 2.1 is the exact repair.  It remains
fractional and supplies no owner partition.

## 3. Integral owner-dependent frame schedule

Fix a coordinate \(z\in[2m+1]\), put

\[
 V=[2m+1]\setminus\{z\},
\]

and use the frozen theorem that exact odd middle-wreath factors exist.
Cutting every wreath at \(z\) gives an exact family \(\mathcal P\) of
complement-ended Johnson geodesics

\[
 P=(X_0,X_1,\ldots,X_m),\qquad X_m=V\setminus X_0,
\tag{3.1}
\]

whose vertices partition \(\binom Vm\).  Its number of paths is

\[
 B={1\over2m+1}\binom{2m+1}{m}
  ={1\over m+1}\binom{2m}{m}
  ={W\over m+1}.
\tag{3.2}
\]

Write the transitions on one path as

\[
 X_{i+1}=X_i-a_i+b_i\qquad(0\le i<m).
\tag{3.3}
\]

Because the path is a geodesic from a set to its complement,

\[
 a_0,\ldots,a_{m-1}\ \hbox{enumerate }X_0,
 \qquad
 b_0,\ldots,b_{m-1}\ \hbox{enumerate }V\setminus X_0.
\tag{3.4}
\]

In particular the \(m\) pairs

\[
 \{a_i,b_i\}\qquad(0\le i<m)
\tag{3.5}
\]

are disjoint.  Extend (3.1) conceptually to the cyclic sequence

\[
 X_0,X_1,\ldots,X_m=X_0^c,
 X_1^c,\ldots,X_{m-1}^c.
\tag{3.6}
\]

Its transition-pair word is

\[
 \{a_0,b_0\},\ldots,\{a_{m-1},b_{m-1}\},
 \{a_0,b_0\},\ldots,\{a_{m-1},b_{m-1}\}.
\tag{3.7}
\]

Thus (3.6) is a \(\pi\pi\) necklace, although \(m\) need not be a power
of two.

Choose \(\ell\) as in (0.2), and set

\[
 s=\ell-2H+1.
\tag{3.8}
\]

Partition the principal index interval \(\{0,1,\ldots,m\}\) of every path
into consecutive chunks \([a,b]\) containing at most \(s\) owners.  Give
the chunk the conceptual collar

\[
 X_{a-H},X_{a-H+1},\ldots,X_{b+H},
\tag{3.9}
\]

with indices interpreted in the cyclic closure (3.6).

### Theorem 3.1 (integral mixed-frame collared schedule)

The chunks above have all of the following exact properties.

1. Their principal owners partition \(\binom Vm\) exactly.
2. Every collared chunk is a segment of a coordinate-conjugated native
   \(F_\ell\)-cycle.
3. Every principal owner carries literal lower and upper flags through
   depth \(H\), including owners within \(H\) of a chunk endpoint.
4. The number \(C\) of chunks satisfies

   \[
   \boxed{
   C\le B\left\lceil{m+1\over\ell-2H+1}\right\rceil
    \le {W\over\ell-2H+1}+{W\over m+1}.}
   \tag{3.10}
   \]

5. In an arbitrary linear ordering of the chunks, the exact useful-prefix
   bridge excess satisfies

   \[
   \boxed{
   \operatorname{Br}\le2H(C-1)
    <{2HW\over\ell-2H+1}+{2HW\over m+1}=o(W).}
   \tag{3.11}
   \]

Equivalently, independently initializing every chunk gives a literal word
of length at most \(W+2HC=W+o(W)\) before missing-target repairs.

#### Proof

Only item 2 needs geometry.  A chunk containing \(t=b-a+1\) principal
owners has

\[
 H+(t-1)+H=t+2H-1\le\ell
\tag{3.12}
\]

collar transitions.  By (3.7), every block of at most \(m\) consecutive
transitions uses distinct pair indices, and \(\ell\le m\).  Take one
native \(F_\ell\)-cycle.  Its first-half transition word uses its \(\ell\)
pairs once.  A permutation of active pairs maps the required consecutive
part of that order to the transitions in (3.9), and independent swaps of
pair endpoints map its starting orientation to \(X_{a-H}\).  If (3.12) is
strict, fill the unused active pairs with arbitrary unused pairs from
(3.5).  This maps the entire collar, not merely its owner set, to a native
cycle segment.

The collar is conceptual in the useful-prefix compiler.  It initializes
the exact radius-\(H\) state at the first principal owner and prescribes the
terminal deletion queue; it is not traversed again as separately owned
middle vertices.  The audited phase compiler gives exact phase length
\(t+2H\).  Future intersections give all lower flags and past unions give
all upper flags, including at both chunk boundaries.  This proves items
1--3.

There are \(B\) paths and at most the displayed ceiling chunks per path,
which proves the first inequality in (3.10).  Applying
\(\lceil x\rceil\le x+1\) and (3.2) gives its second inequality.

Every useful-prefix bridge has length at most \(2H+1\), hence excess at
most \(2H\).  There are \(C-1\) bridges.  Equations (3.10), (0.2), and
\(\ell-2H+1\sim\ell\) prove (3.11).  \(\square\)

### Corollary 3.2 (largest-power constants)

Let \(\ell\) be the largest power of two not exceeding \(m\).  For all
sufficiently large \(m\),

\[
 \left\lceil{m+1\over\ell-2H+1}\right\rceil\le3.
\tag{3.13}
\]

Consequently (0.4) holds.

#### Proof

One has \(m\le2\ell-1\).  Since \(H/\ell\to0\), eventually
\(\ell-6H+3\ge0\), and therefore

\[
 3(\ell-2H+1)\ge2\ell\ge m+1.
\]

This proves (3.13); substitute it into (3.10)--(3.11).  \(\square\)

### Corollary 3.3 (the schedule genuinely mixes frames)

The number of distinct full pair frames appearing among the paths is at
least

\[
 {W\over2^m}\sim {2^m\over\sqrt{\pi m}}.
\tag{3.14}
\]

#### Proof

Every owner on a path splits the path frame (3.5).  One fixed perfect
matching has exactly \(2^m\) transversal middle owners.  Since the path
owners partition all \(W\) middle sets, at least \(W/2^m\) distinct
frames are necessary.  \(\square\)

Thus Theorem 3.1 is not a disguised fixed-frame construction and is not
subject to the fixed-frame Gaussian capacity obstruction.

## 4. Exact cross-path shadow ledger

Encode one conceptual closure (3.6) by a cyclic list
\(w_0,\ldots,w_{2m-1}\) so that

\[
 X_i=I_w(i,m).
\tag{4.1}
\]

For every selected principal index \(0\le i\le m\), Theorem 1.1 gives

\[
 L_q(i)=I_w(i+q,m-q),
\tag{4.2}
\]

\[
 U_q(i)=I_w(i-q,m+q),
\tag{4.3}
\]

and hence

\[
 V\setminus U_q(i)=I_w(i+m,m-q).
\tag{4.4}
\]

For one path \(P\), define

\[
 \widehat{\mathcal I}_q^-(P)
 =\{I_w(i+q,m-q):0\le i\le m\},
\tag{4.5}
\]

and define the complemented upper family

\[
 \widehat{\mathcal I}_q^{+,c}(P)
 =\{I_w(i+m,m-q):0\le i\le m\}.
\tag{4.6}
\]

All \(m+1\) members of either family are distinct when \(q<m\).  Put

\[
 S_q^-=\bigcup_{P\in\mathcal P}\widehat{\mathcal I}_q^-(P),
 \qquad
 S_q^{+,c}=\bigcup_{P\in\mathcal P}
                    \widehat{\mathcal I}_q^{+,c}(P).
\tag{4.7}
\]

Define

\[
 S_q^+=\{V\setminus T:T\in S_q^{+,c}\}.
\tag{4.7a}
\]

Thus \(S_q^+\) is the actual advertised upper support and
\(|S_q^+|=|S_q^{+,c}|\).

### Theorem 4.1 (guaranteed hole and duplicate ledger)

The literal chronology constructed in Theorem 3.1 satisfies

\[
 \boxed{
 \operatorname{Hol}_{\rm actual}
 \le\sum_{q=1}^H
 \bigl[(N_q-|S_q^-|)+(N_q-|S_q^+|)\bigr].}
\tag{4.8}
\]

For either sign, let \(\lambda_q(T)\) be the number of path/index pairs in
(4.5) or (4.6) producing \(T\), and put

\[
 M_q=\#\{T:\lambda_q(T)=0\},\qquad
 R_q=\sum_T(\lambda_q(T)-1)_+.
\tag{4.9}
\]

Then exactly

\[
 \boxed{M_q=R_q-(W-N_q).}
\tag{4.10}
\]

#### Proof

The conceptual collars in Theorem 3.1 reproduce (4.2)--(4.3) literally at
every principal owner, including chunk boundaries.  Thus every member of
(4.7) is witnessed by an interval in the compiled word.  Bridge-crossing
and incidental intervals may add targets but cannot delete any, proving
(4.8).

There is one advertised signed depth-\(q\) flag at each of the \(W\)
principal owners, so \(\sum_T\lambda_q(T)=W\).  Splitting this sum over
zero, unit, and overloaded targets gives

\[
 W-N_q=R_q-M_q,
\]

which is (4.10).  \(\square\)

### Depth-one audit

The \(m\) internal upper unions on every complementary path partition
\(\binom V{m+1}\) across the exact odd-cut path factor.  Hence the upper
support in (4.7) is complete at \(q=1\); the additional closure flag is
harmless surplus.

There is no corresponding unconditional statement for the internal lower
intersections.  Their holes are exactly the fixed-coordinate form of the
first-shadow defect of the chosen exact wreath factor, up to the displayed
cap/closure occurrences.  Declaring the lower depth-one deficiency zero
would assume the unresolved first-shadow/MWB theorem.  This distinction is
essential.

More precisely, the closure adds only one lower occurrence per path.  If
\(M_{1,\mathrm{int}}^-\) is the hole count from the \(m\) internal
intersections per path and \(M_{1,\mathrm{cl}}^-\) is the count after the
extra closure flag, then

\[
 0\le M_{1,\mathrm{int}}^- - M_{1,\mathrm{cl}}^-\le B=o(W).
\tag{4.11}
\]

Thus the two lower depth-one \(o(W)\) assertions are asymptotically
equivalent, but neither is proved here.

## 5. A capacitated-Hall sufficient estimate

The support condition in Section 4 has a useful exact strengthening.  Put

\[
 s_q=\left\lfloor{N_q\over B}\right\rfloor
    =\left\lfloor{(m+1)N_q\over W}\right\rfloor,
\tag{5.1}
\]

and, for either signed family, define

\[
 \widehat\delta_q^\pm
 =\max_{\mathcal X\subseteq\mathcal P}
 \left(
 s_q|\mathcal X|-
 \left|\bigcup_{P\in\mathcal X}
       \widehat{\mathcal I}_q^\pm(P)\right|
 \right)_+.
\tag{5.2}
\]

For the upper sign, targets are understood after complementation as in
(4.6).

### Theorem 5.1 (exact path-to-target Hall bound)

For either sign,

\[
 \boxed{N_q-|S_q^\pm|<B+\widehat\delta_q^\pm.}
\tag{5.3}
\]

Consequently

\[
 \boxed{
 \operatorname{Hol}_{\rm actual}
 <{2HW\over m+1}
  +\sum_{q=1}^H
   (\widehat\delta_q^-+\widehat\delta_q^+).}
\tag{5.4}
\]

In particular, (0.6) implies \(\operatorname{Hol}_{\rm actual}=o(W)\),
and Theorem 3.1 then proves \(\mathrm{MFUP}_A\) for this path factor.

#### Proof

Form a bipartite graph with left side \(\mathcal P\), right side the
rank-\((m-q)\) targets, and neighborhoods
\(\widehat{\mathcal I}_q^\pm(P)\).  Give each left vertex demand \(s_q\)
and each target capacity one.  The capacitated Hall deficiency formula says
that the maximum matching size is

\[
 Bs_q-\widehat\delta_q^\pm.
\tag{5.5}
\]

Indeed, replacing every path by \(s_q\) identical clones reduces this to
ordinary Hall; a worst deficient clone set may be completed to all clones
of every path it meets, so (5.2) is the exact deficiency.  Every matched
target belongs to \(S_q^\pm\), whence

\[
 |S_q^\pm|\ge Bs_q-\widehat\delta_q^\pm.
\]

Write \(N_q=Bs_q+f_q\), where \(0\le f_q<B\).  Rearrangement proves
(5.3).  Sum (5.3) over both signs and \(q\le H\), use
\(B=W/(m+1)\), and apply (4.8) to obtain (5.4).  Finally

\[
 HB={HW\over m+1}=O_A(W/\sqrt m)=o(W).
\]

Together with (3.11), this is exactly the MFUP conclusion.  \(\square\)

The estimate (0.6) is a real remaining theorem, not a restatement of a
local availability condition.  At upper depth one it holds with zero
deficiency by the exact union partition.  At lower depth one, even the
weaker global assertion \(N_1-|S_1^-|=o(W)\) is not known for an arbitrary
exact wreath factor.

## 6. Collar stability and the no-new-support boundary

The preceding construction deliberately chooses collars from the
conceptual closure.  Could unused pair completions or other native
\(F_\ell\) phases repair bad cross-path support without changing the owned
interiors?  Only boundary flags can change.

### Theorem 6.1 (exact boundary-edit bound)

Fix a decomposition into \(C\) oriented Johnson-path pieces and keep every
owned interior transition fixed.  Compare two legal radius-\(H\) collar
completions of these pieces.  At depth \(q\le H\):

* their lower advertised flags can differ only at the final \(q\) owners
  of each piece;
* their upper advertised flags can differ only at the initial \(q\) owners
  of each piece.

Thus at most \(qC\) signed occurrences change, and for either sign

\[
 \boxed{M_q^{\rm new}\ge M_q^{\rm old}-qC.}
\tag{6.1}
\]

#### Proof

At an owner having at least \(q\) retained successors in its piece, the
lower flag is the intersection of those \(q+1\) fixed consecutive owners.
It is independent of the terminal collar.  Only the last \(q\) owners can
see a changed future.  The reverse statement gives the first \(q\) owners
for upper flags.  Replacing one occurrence value can enlarge support by at
most one, which proves (6.1).  \(\square\)

For the largest-power schedule, \(C\le3W/(m+1)\), and therefore, uniformly
for \(q\le H\),

\[
 qC=O_A(W/\sqrt m)=o(W).
\tag{6.2}
\]

Hence a positive-density hole deficit in the **advertised collar ledger**
at any one Gaussian depth cannot be removed merely by changing unused pair
completions or collar phases while retaining the \(O(W/m)\)-piece
interiors.  This statement deliberately does not bound incidental intervals
created by the eventual bridges.  A bridge position may belong to many
longer intervals ending later, so \(\operatorname{Br}=o(W)\) alone is not a
support bound for those incidental witnesses.

Theorem 6.1 is not a universal MFUP lower bound.  A successful construction
may change a positive fraction of path interiors, use higher-order trades
among several owner resolutions, or exploit a new correlated path factor.
It says precisely that the recursive collars alone do not supply the
missing cross-component support.

## 7. The integral selection matrix is not TU

We now audit the tempting flow-rounding shortcut directly.

Let \(R=2\ell\), assume

\[
 3(\ell-1)\le m-2,
\tag{7.1}
\]

and choose an \((m-1)\)-set \(K\) and distinct coordinates
\(a,b,c\notin K\).  Put

\[
 X_a=K+a,\qquad X_b=K+b,\qquad X_c=K+c.
\tag{7.2}
\]

For each of the pairs \(ab,bc,ca\), choose \(\ell-1\) distinct elements of
\(K\) and \(\ell-1\) distinct elements outside \(K\cup\{a,b,c\}\), with
all six groups disjoint across the three choices.  This is possible by
(7.1).  Make the special pair, for example \(\{a,b\}\), and these
\(\ell-1\) auxiliary pairs the active pairs of an orientation cube.  Map
one native \(F_\ell\)-cycle edge to

\[
 X_a\longrightarrow X_b.
\]

Call the resulting necklace \(B_{ab}\), and define \(B_{bc},B_{ca}\)
cyclically.

### Lemma 7.1 (exact triangle intersections)

The three genuine necklaces satisfy

\[
 B_{ab}\cap B_{bc}=\{X_b\},\quad
 B_{bc}\cap B_{ca}=\{X_c\},\quad
 B_{ca}\cap B_{ab}=\{X_a\},
\tag{7.3}
\]

and have empty triple intersection.  Their union has size \(3R-3\).

#### Proof

It suffices to intersect the ambient orientation cubes.  Relative to
\(X_b\), the \(ab\)-cube has binary span generated by the toggle
\(\mathbf e_a+\mathbf e_b\) and its private auxiliary pair toggles.  The
\(bc\)-cube has span generated by
\(\mathbf e_b+\mathbf e_c\) and a disjoint private auxiliary family.  A
nonzero vector in both spans cannot use a private coordinate.  It also
cannot use the special generator on either side: the first would expose
coordinate \(a\), and the second coordinate \(c\), with no generator on the
other side available to cancel it.  Thus the two spans meet only at zero,
and the cubes meet only at \(X_b\).  The other identities follow
cyclically.  The shared owners are distinct, so there is no triple
intersection.  Inclusion--exclusion gives \(3R-3\).  \(\square\)

### Corollary 7.2 (minimal non-TU minor)

On rows \(X_a,X_b,X_c\) and columns \(B_{ab},B_{bc},B_{ca}\), the
middle-owner incidence matrix contains

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
\qquad \det=2.
\tag{7.4}
\]

Hence neither the owner matrix nor any larger matrix retaining these rows
and columns is totally unimodular.  This is dimension-minimal, since every
\(0\)-\(1\) matrix of order at most two has determinants only
\(0,\pm1\).

Adding target-cover inequalities, hole variables, or singleton residual
columns cannot restore TU: total unimodularity is inherited by submatrices.

### Proposition 7.3 (genuine local LP gap)

Restrict the owner-cover problem on

\[
 \mathcal U=B_{ab}\cup B_{bc}\cup B_{ca}
\]

to the three necklace columns and one singleton residual column for every
owner.  Minimize total singleton residual mass subject to exact owner load
one.  Then

\[
 E_{\rm frac}={3(R-2)\over2},
 \qquad
 E_{\rm int}=2R-3,
\tag{7.5}
\]

so

\[
 \boxed{E_{\rm int}-E_{\rm frac}={R\over2}=\ell.}
\tag{7.6}
\]

The ratio tends to \(4/3\).

#### Proof

Fractionally give each necklace weight \(1/2\).  Every shared owner lies
in two necklaces and has load one.  Every necklace has \(R-2\) private
owners; give each corresponding singleton weight \(1/2\).  This proves the
first value in (7.5).  For optimality, if the three necklace weights are
\(z_1,z_2,z_3\), the shared-owner constraints give
\(z_i+z_j\le1\) for every pair and hence
\(z_1+z_2+z_3\le3/2\).  After exact singleton completion, the objective is

\[
 (3R-3)-R(z_1+z_2+z_3),
\]

because every selected necklace unit replaces exactly \(R\) singleton
units.  Its minimum is therefore attained at
\(z_1=z_2=z_3=1/2\), proving the fractional optimum.

Integrally, no two necklaces may be selected because every pair overlaps.
Selecting one is better than selecting none and leaves

\[
 |\mathcal U|-R=(3R-3)-R=2R-3
\]

singleton owners.  This proves the second value and (7.6).  \(\square\)

This is an exact local obstruction to support-preserving or purely local
rounding.  It is not a counterexample to full MFUP: the unrestricted library
contains necklaces crossing \(\mathcal U\) and its complement.

## 8. Exact orbit codegrees

The same library nevertheless has very small middle pair-codegrees.  This
explains why fractional and fixed-accuracy nibble statements are plausible
while showing that small codegree is not an integrality theorem.

Take the indexed orbit of one \(R=2\ell\) necklace under
\(G=S_{2m}\).  Its owner degree is

\[
 D={|G|R\over W}=R(m!)^2.
\tag{8.1}
\]

### Proposition 8.1 (exact indexed pair-codegrees)

If two middle owners have Johnson distance \(j\), their indexed orbit
codegree is

\[
 \boxed{
 \lambda_j=
 \begin{cases}
 \displaystyle {2D\over\binom mj^2},&1\le j<\ell,\\[6pt]
 \displaystyle {D\over\binom m\ell^2},&j=\ell,\\[6pt]
 0,&j>\ell.
 \end{cases}}
\tag{8.2}
\]

In particular

\[
 {\max_{X\ne Y}\lambda(X,Y)\over D}={2\over m^2}.
\tag{8.3}
\]

Every Johnson triangle has necklace triple-codegree zero.

#### Proof

In a cyclic-interval necklace, for every \(1\le j<\ell\), each of the
\(R\) positions has two ordered positions at distance \(j\), giving
\(2R\) ordered base pairs.  At \(j=\ell\), only the antipode remains,
giving \(R\) ordered base pairs.  There are none at larger Johnson
distance.

The stabilizer of a fixed ordered pair of middle sets at distance \(j\)
has size

\[
 (m-j)!^2(j!)^2.
\tag{8.4}
\]

Multiplying the base-pair counts by (8.4) and dividing by
\(D=R(m!)^2\) gives (8.2).  Ordered base pairs introduce no extra factor:
for a fixed relabelling containing \(X,Y\), exactly one ordered base pair
maps to the fixed ordered pair \((X,Y)\).

An orientation cube is bipartite, so it contains no Johnson triangle.
Every necklace lies inside one such cube, proving the triple-codegree
claim.  \(\square\)

The condition (8.3) alone yields neither the \(o(W/H)\) owner residual
needed for singleton cleanup nor the simultaneous signed shadow bound
\(o(W)\).  Proposition 7.3 gives the first exact local reason that no
generic TU rounding theorem is available.

## 9. Final implication boundary

### Proved

1. Every embedded recursive \(F_\ell\)-cycle has the exact
   cyclic-interval normal form (1.6)--(1.8).
2. One native coordinate orbit already contains every individual
   core-lifted necklace atom.
3. A two-sided collar repairs the fractional open-segment loss for every
   \(H=o(\ell)\le m\), with exact fractional toll \(HW/\ell\).
4. Every exact odd-cut complementary-path factor has an integral
   owner-dependent \(F_\ell\)-schedule satisfying (0.3); for maximal
   \(\ell\), the sharp convenient bounds are (0.4).
5. The schedule preserves all chosen closure flags literally through
   depth \(H\), including chunk boundaries.
6. The exact support, duplicate, and capacitated-Hall ledgers are
   (4.8)--(5.4).
7. Changing only collars affects at most \(qC\) flags of either sign at
   depth \(q\).
8. Under \(3(\ell-1)\le m-2\), the whole-necklace owner matrix contains
   the determinant-two minor (7.4), and the restricted genuine instance
   has additive LP gap \(\ell\).
9. The indexed orbit pair-codegrees are exactly (8.2).

### Unproved

1. Existence of an exact complementary-path factor satisfying

   \[
   \sum_{q=1}^H
   \bigl[(N_q-|S_q^-|)+(N_q-|S_q^+|)\bigr]=o(W),
   \tag{9.1}
   \]

   or the stronger Hall estimate (0.6).
2. Any global rounding theorem overcoming the determinant-two packet
   trades while preserving both signed shadows.
3. An \(o(W/H)\)-residual quantitative matching theorem for the growing
   necklace uniformity that also controls all depth rows.

### Exact conclusion

The recursive orientation-cube cycles do solve the **integral mixed-frame
schedule** part of MFUP: exact owners, genuinely varying frames, legal
radius-\(H\) states, literal collars, and \(o(W)\) interfaces coexist in
one construction.  They do not solve the **cross-component selected
support** part.  After Theorem 1.1, that remaining term is precisely an
interval-support/Hall theorem for the complementary paths of one exact
wreath factor.  The lower depth-one slice already contains the unresolved
first-shadow gate, and the determinant-two gadget rules out a generic
flow-integrality shortcut.

Accordingly no coefficient-one conclusion is claimed.
