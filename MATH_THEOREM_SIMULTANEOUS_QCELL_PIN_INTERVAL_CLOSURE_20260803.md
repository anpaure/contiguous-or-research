# Simultaneous (q)-cell pins are an exact interval-closure problem

**Date:** 2026-08-03  
**Status:** unconditional exact simultaneous-realization theorem for a fixed
cyclic carrier, exact run-local obstruction, and a bounded-defect protected
transversal criterion.  No computational input is used.  This does **not**
construct the required carrier or the target-to-cell assignment.

## 0. Outcome

Let \(0<r<k\), put \(W={k\choose r}\), and let

\[
 T_0,T_1,\ldots,T_{W-1}\in {[k]\choose r}
\]

be a cyclic Johnson carrier which visits the complete rank-\(r\) layer once,
with all indices in \(\mathbb Z_W\).  Write

\[
                  T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.          \tag{0.0}
\]

Assume as a standing hypothesis that every positive coordinate run has
length at least \(d+1\).  Put

\[
 E_h=\bigcap_{i=h-d}^{h}T_i,
 \qquad
 E_{j,q}=\bigcup_{h=j}^{j+q-1}E_h
             =\bigcap_{i=j+q-1-d}^{j}T_i                 \tag{0.1}
\]

for \(1\le q\le d\).  The mandatory collar of the physical cell
\(c=(j,q)\) is

\[
 K_c=
 \{\alpha_j,\ldots,\alpha_{j+q-1}\}
 \cup
 \{\beta_{j-d-1},\ldots,\beta_{j+q-d-2}\}.             \tag{0.2}
\]

Fix any family of **distinct** physical cells \(c\), and prescribe one target
\(S_c\) at each of them, subject only to the individual aperture conditions

\[
                 K_c\subseteq S_c\subseteq E_c.         \tag{0.3}
\]

For a coordinate \(x\), let

\[
 R_x=\{h:x\in E_h\}                                    \tag{0.4}
\]

be its erosion support, and declare forbidden every source position lying
in a selected cell whose target omits \(x\):

\[
 F_x=R_x\cap
 \bigcup_{c:x\notin S_c}I_c,
 \qquad
 U_x=R_x\setminus F_x,                                 \tag{0.5}
\]

where \(I_c=[j,j+q-1]_W\) is the forward cyclic interval of the cell.

Then all the cell equations

\[
                   \bigcup_{h\in I_c}A_h=S_c           \tag{0.6}
\]

are simultaneously realizable by one depth-\(d\) factor if and only if the
following two visibly necessary conditions hold:

\[
\begin{array}{ll}
\textbf{owner hitting:}&
 [i,i+d]_W\cap U_x\ne\varnothing
       \quad(x\in T_i),\\[2mm]
\textbf{positive-cell hitting:}&
 I_c\cap U_x\ne\varnothing
       \quad(x\in S_c).
\end{array}                                             \tag{0.7}
\]

There is no further interaction between coordinates and no hidden Hall
condition.  When (0.7) holds, the coordinatewise greatest realizing factor
is explicit:

\[
                       A_h^*=\{x:h\in U_x\}.            \tag{0.8}
\]

The owner condition has an especially simple run-local form.  On every
maximal positive \(x\)-run, let \(R\) be its erosion interval.  Then owner
hitting fails exactly when

\[
             F_x\cap R\text{ contains }d+1
             \text{ consecutive source positions}.    \tag{0.9}
\]

Equivalently, every connected forbidden block inside every erosion interval
must have size at most \(d\).  A positive selected cell fails exactly when
its nonempty aperture \(I_c\cap R_x\) is covered by the negative selected
cell intervals for \(x\).

Thus simultaneous pinning is an interval-cover closure problem.  For each
coordinate, the zero-labelled selected intervals generate a closure; an
owner interval or a one-labelled selected interval may not lie in that
closure.  The associated independence system is generally **not** a
matroid.  Its exact certificate is instead a family of protected occurrence
points, and its exact obstruction is a chain of negative intervals covering
one required interval.

In particular, if all but \(C\) lower targets admit distinct cell assignments
and protected occurrence sets satisfying (0.7), the fixed carrier has lower
compiler defect at most \(C\).  This is the proof-safe form needed by any
bounded-literal-deficiency terminal theorem.

## 1. Cyclic conventions and erosion geometry

Assume throughout that

\[
                         1\le d<W.                    \tag{1.1}
\]

The case \(d=0\) has no strict-lower \(q\)-cells and is empty.  A cyclic
interval \([a,a+\ell-1]_W\), \(1\le\ell<W\), always means the forward arc
of exactly \(\ell\) source positions.  Thus a cell interval is unambiguous
even when it crosses the displayed index \(W-1\mid0\).

Because \(0<r<k\), every coordinate is absent from at least one carrier
owner.  Its positive owner set therefore decomposes canonically into proper
cyclic runs.  Lift one such run to

\[
                         T_s,T_{s+1},\ldots,T_t.       \tag{1.2}
\]

The standing run-floor hypothesis gives \(t-s+1\ge d+1\).  The corresponding
erosion support is

\[
                         R=[s+d,t].                   \tag{1.3}
\]

Indeed, \(x\in E_h\) precisely when all owners
\(T_{h-d},\ldots,T_h\) lie in the positive run.

### Lemma 1.1 (erosion runs are well separated)

Distinct erosion intervals of one coordinate are separated cyclically by
at least \(d+1\) source positions outside the erosion support.  Consequently
every cell interval of length at most \(d\) meets at most one erosion
interval of a fixed coordinate.

#### Proof

If one positive run ends at \(t\) and the next starts at \(s'\), then at
least one owner between them omits \(x\), so \(s'\ge t+2\) in a common
cyclic lift.  The next erosion interval begins at \(s'+d\).  The positions

\[
                    t+1,\ldots,s'+d-1
\]

therefore number \((s'-t-1)+d\ge d+1\).  A forward interval of length at
most \(d\) cannot cross this gap and meet both erosion intervals. \(\square\)

For an owner \(T_i\) in the run (1.2), the positions at which \(x\) can
supply that owner are exactly

\[
 D_{x,i}:=[i,i+d]\cap[s+d,t]
   =[\max(i,s+d),\min(i+d,t)].                         \tag{1.4}
\]

This interval is always nonempty.

### Lemma 1.2 (erosion endpoints cannot be forbidden)

Under the individual aperture conditions (0.3), neither endpoint of an
erosion interval belongs to \(F_x\).

#### Proof

At the left endpoint \(s+d\), the coordinate is the forced arrival

\[
                       x=\beta_{s-1}
                         =\beta_{(s+d)-d-1}.          \tag{1.5}
\]

At the right endpoint \(t\), it is the forced departure

\[
                       x=\alpha_t.                    \tag{1.6}
\]

If a selected cell interval contains either endpoint \(h\), then its
mandatory collar contains the complete one-position footprint
\(\{\alpha_h,\beta_{h-d-1}\}\).  Hence its target contains \(x\), and that
cell cannot contribute \(h\) to the forbidden set for \(x\). \(\square\)

This endpoint fact is what makes the cyclic boundary harmless.  It is also
why the owner obstruction below is a full \((d+1)\)-block rather than a
short clipped block at the end of a run.

### Lemma 1.3 (the exact \(q\)-cell upper aperture)

For every \(1\le q\le d\),

\[
 \bigcup_{h=j}^{j+q-1}E_h
   =\bigcap_{i=j+q-1-d}^{j}T_i.                       \tag{1.7}
\]

#### Proof

If \(x\in E_h\) for some \(j\le h\le j+q-1\), then the owner interval
\([j+q-1-d,j]\) is contained in \([h-d,h]\), so \(x\) belongs to every owner
on the right.

Conversely, suppose \(x\) belongs throughout \([j+q-1-d,j]\), and lift the
positive run containing this owner interval to \([s,t]\).  Then

\[
                         s+d\le j+q-1,\qquad t\ge j.  \tag{1.8}
\]

Its erosion interval \([s+d,t]\) therefore meets \([j,j+q-1]\), so
\(x\in E_h\) for some \(h\) in the cell.  The argument is unchanged when
the displayed cell crosses the cyclic index boundary: cut at a negative
owner of \(x\) and use the corresponding lift. \(\square\)

## 2. Exact simultaneous-realization theorem

Let \({\cal C}\) be the selected set of distinct cells.  For every
coordinate \(x\), define two families of required intervals:

\[
\begin{aligned}
 {\cal O}_x&=\{[i,i+d]_W\cap R_x:x\in T_i\},\\
 {\cal P}_x&=\{I_c\cap R_x:c\in{\cal C},\ x\in S_c\}.
                                                               \tag{2.1}
\end{aligned}
\]

Every member of \({\cal P}_x\) is nonempty: if \(x\in S_c\subseteq E_c\),
then \(x\in E_h\) for some \(h\in I_c\).  Lemma 1.1 says it lies in a
unique erosion interval.

### Theorem 2.1 (simultaneous (q)-cell pin criterion)

The following are equivalent.

1. There are nonempty source letters \(A_h\subseteq E_h\) such that

   \[
       T_i=\bigcup_{h=i}^{i+d}A_h
       \quad(i\in\mathbb Z_W),
       \qquad
       S_c=\bigcup_{h\in I_c}A_h
       \quad(c\in{\cal C}).                           \tag{2.2}
   \]

2. For every coordinate \(x\), every required interval meets the allowed
   erosion support:

   \[
               B\cap U_x\ne\varnothing
               \qquad(B\in{\cal O}_x\cup{\cal P}_x).  \tag{2.3}
   \]

3. No required interval is covered by selected cells whose targets omit
   the coordinate:

   \[
       B\not\subseteq
       \bigcup_{c:x\notin S_c}I_c
       \qquad(B\in{\cal O}_x\cup{\cal P}_x).           \tag{2.4}
   \]

When these conditions hold, (0.8) is a realizing factor.  Moreover every
other realizing factor \((A_h)\) satisfies \(A_h\subseteq A_h^*\) for all
\(h\).

#### Proof

Suppose first that \((A_h)\) realizes all equations, and put

\[
                         Z_x=\{h:x\in A_h\}.          \tag{2.5}
\]

Since \(A_h\subseteq E_h\), one has \(Z_x\subseteq R_x\).  If a selected
cell target omits \(x\), its union equation forces
\(Z_x\cap I_c=\varnothing\).  Thus

\[
                         Z_x\subseteq U_x.            \tag{2.6}
\]

Every owner containing \(x\), and every selected target containing \(x\),
requires its interval to meet \(Z_x\).  It therefore meets \(U_x\), proving
(2.3).  Conditions (2.3) and (2.4) are the same statement by (0.5).

Conversely, assume (2.3) and define \(A_h^*\) by (0.8).  Since
\(U_x\subseteq R_x\), every \(A_h^*\) is contained in \(E_h\), so no owner
or selected cell acquires an extraneous coordinate.

If \(x\in T_i\), the required owner interval in \({\cal O}_x\) meets
\(U_x\), and hence \(x\in\bigcup_{h=i}^{i+d}A_h^*\).  Thus every owner
coordinate is supplied.

If \(x\notin S_c\), then \(I_c\) is one of the intervals removed in the
definition of \(U_x\), so \(I_c\cap U_x=\varnothing\).  If \(x\in S_c\),
the corresponding interval in \({\cal P}_x\) meets \(U_x\).  Therefore
the cell union is exactly \(S_c\).

It remains only to check that no source letter is empty.  For each position
\(h\), the departure coordinate \(\alpha_h\) lies in \(E_h\).  No selected
cell omitting \(\alpha_h\) can contain \(h\), because every such cell has
\(\alpha_h\in K_c\subseteq S_c\).  Hence \(h\in U_{\alpha_h}\), and
\(\alpha_h\in A_h^*\).  Thus \(A_h^*\ne\varnothing\).

Finally, (2.6) applies to every realizing factor, proving coordinatewise
maximality. \(\square\)

### Corollary 2.2 (no cross-coordinate capacity obstruction)

For a fixed target-to-cell assignment, simultaneous factorability splits
exactly into \(k\) independent interval-hitting tests.  Physical source
positions have no capacity coupling across coordinates: the same position
may supply arbitrarily many coordinates, subject only to membership in its
erosion set.

This is why a matroid-intersection or multicommodity-flow theorem is not the
missing fixed-assignment theorem.  All of the difficulty is already visible
as interval coverage after the assignment is fixed.

## 3. Owner failure is one forbidden run

### Theorem 3.1 (run-local owner criterion)

For a fixed coordinate \(x\), all owner intervals in \({\cal O}_x\) meet
\(U_x\) if and only if, on every erosion interval \(R\), every consecutive
component of \(F_x\cap R\) has cardinality at most \(d\).

Equivalently, owner failure occurs if and only if there is an erosion
interval \(R\) and a source position \(h\) such that

\[
              [h,h+d]\subseteq R\cap F_x.            \tag{3.1}
\]

#### Proof

If (3.1) holds, then \(h\) itself lies in the positive owner run and the
supplier interval for owner \(T_h\) is the full interval \([h,h+d]\).
It contains no allowed occurrence of \(x\), so that owner fails.

Conversely, suppose owner \(T_i\) fails.  Its supplier interval
\(D_{x,i}\) from (1.4) lies in \(F_x\).  If it is clipped at the left end of
the erosion interval, it contains the left erosion endpoint; if clipped at
the right, it contains the right endpoint.  Lemma 1.2 rules out both cases.
Hence it is un-clipped, has exactly \(d+1\) consecutive positions, and has
the form (3.1). \(\square\)

### Corollary 3.2 (complete fixed-assignment obstruction list)

The selected pins fail simultaneously if and only if at least one of the
following occurs.

1. **Owner cover:** for some coordinate, negative selected cell intervals
   cover \(d+1\) consecutive positions inside one erosion interval.
2. **Positive-aperture cover:** for some selected cell \(c\) and some
   \(x\in S_c\), the negative selected cell intervals for \(x\) cover the
   nonempty interval \(I_c\cap R_x\).

There are no other simultaneous-pin failures.

## 4. Interval closure, cover chains, and why this is not a matroid

For a fixed coordinate, let \({\cal I}_x\) consist of all relevant
owner-supplier intervals together with every nonempty selected-cell interval
clipped to \(R_x\), whether that cell is positive or negative for \(x\).
For a family \({\cal N}\subseteq{\cal I}_x\) of negative clipped cell
intervals define

\[
 \operatorname{cl}_x({\cal N})=
 \left\{B\in{\cal I}_x:
 B\subseteq\bigcup_{I\in{\cal N}}I\right\}.            \tag{4.1}
\]

This is a closure operator on \({\cal I}_x\): it is extensive, monotone, and
idempotent.  Theorem 2.1 says exactly

\[
 \boxed{
   \text{all owner and positive intervals lie outside the closure
   generated by the negative intervals.}}
                                                               \tag{4.2}
\]

### Proposition 4.1 (minimal obstruction certificate)

Let \(B=[a,b]\) be a required interval in a linear lift of one erosion run.
Then \(B\subseteq\bigcup_{I\in{\cal N}}I\) if and only if there is a sequence

\[
                       I_1,I_2,\ldots,I_m\in{\cal N}  \tag{4.3}
\]

such that

* \(a\in I_1\) and \(b\in I_m\);
* after clipping to \(B\), the left endpoints strictly increase;
* the right endpoints strictly increase; and
* consecutive intervals overlap or touch in the discrete sense:
  the next left endpoint is at most the preceding right endpoint plus one.

A minimal cover always has this form.

#### Proof

The displayed conditions plainly make the union cover every position from
\(a\) through \(b\).  Conversely, start with an interval containing \(a\)
whose right endpoint is maximal.  If it does not reach \(b\), choose among
all intervals beginning by the next uncovered position one whose right
endpoint is maximal, and continue.  Coverage guarantees that the process
cannot stop before \(b\).  Removing redundant intervals makes both endpoint
sequences strict. \(\square\)

Thus every failure has a short, purely combinatorial cover-chain witness.
For an owner failure, the covered interval has exactly \(d+1\) positions.

### Proposition 4.2 (the pin independence system is not a matroid)

Even one required interval gives a nonmatroidal independence system.

#### Proof

Take the required discrete interval \(B=[1,3]\) and three possible negative
pins with intervals

\[
                       a=[1,2],\qquad b=[1,1],
                       \qquad c=[2,3].                \tag{4.4}
\]

Call a subfamily independent when it does not cover \(B\).  Then
\(\{a,b\}\) is maximal independent of size two, while \(\{c\}\) is maximal
independent of size one: adding either \(a\) or \(b\) to \(\{c\}\) covers
\(B\).  Maximal independent sets have different sizes, so this is not a
matroid. \(\square\)

The correct bipartite representation is simpler.  For each \(x\), form the
convex bipartite graph whose left vertices are
\({\cal O}_x\cup{\cal P}_x\), whose right vertices are the allowed positions
\(U_x\), and whose edges are containment incidences \(h\in B\).  Theorem 2.1
requires only that no left vertex be isolated.  It is **not** a matching
problem, because one occurrence position may witness many interval
obligations.

## 5. Exact mixed-integer assignment formulation

The target-to-cell choice itself still contains a matching constraint.
The following zero-one system cleanly separates that matching from physical
realization.

Let \(y_{S,c}\) say that target \(S\) is assigned to cell \(c\), and let
\(z_{x,h}\) say that coordinate \(x\) is placed at source position \(h\).
Discard in advance every pair not satisfying \(K_c\subseteq S\subseteq E_c\).
For maximum-cardinality compilation, use

\[
\begin{aligned}
 &\sum_c y_{S,c}\le1 &&\text{for every target},\\
 &\sum_S y_{S,c}\le1 &&\text{for every cell},\\
 &z_{x,h}\le {\bf 1}_{\{x\in E_h\}},\\
 &\sum_{h\in[i,i+d]_W}z_{x,h}\ge1 &&(x\in T_i),\\
 &z_{x,h}+y_{S,c}\le1
     &&(h\in I_c,\ x\notin S),\\
 &\sum_{h\in I_c}z_{x,h}\ge y_{S,c}
     &&(x\in S),\\
 &y_{S,c},z_{x,h}\in\{0,1\}.                         \tag{5.1}
\end{aligned}
\]

and maximize

\[
                         \sum_{S,c}y_{S,c}.            \tag{5.2}
\]

To demand a full compiler, replace the first inequalities by equalities.

The source-letter nonemptiness inequalities may be added, but are redundant
after maximalizing the \(z\)'s: the forced departure \(\alpha_h\) is always
legal at position \(h\) and cannot be forbidden by an aperture-compatible
assignment.

For every **fixed integral** \(y\), projection onto the \(z\)-coordinates is
feasible exactly when the interval-cover conditions of Theorem 2.1 hold.
Thus (5.1)--(5.2) is an exact mixed-integer formulation.  This statement
does not assert that its linear relaxation is integral or totally
unimodular.  It shows precisely where integrality remains: the
target-to-cell matching and the interval-cover avoidance must be selected
in correlation.  Ordinary bipartite matching alone forgets the cover
clutter, while ordinary matroid intersection is unavailable by Proposition
4.2.

## 6. Protected occurrence certificates and bounded defect

The exact theorem has a useful certificate form which is better suited to
an all-dimensional construction.

### Theorem 6.1 (protected occurrence or sentinel criterion)

For every coordinate \(x\), suppose one is given a set

\[
                         Z_x\subseteq R_x             \tag{6.1}

\]

such that

\[
\begin{array}{ll}
\text{mandatory footprint:}&
 \{h:\alpha_h=x\text{ or }\beta_{h-d-1}=x\}\subseteq Z_x,\\[1mm]
\text{owner net:}&[i,i+d]_W\cap Z_x\ne\varnothing
                       \quad(x\in T_i),\\[1mm]
\text{cell signature:}&I_c\cap Z_x\ne\varnothing
                       \quad\Longleftrightarrow\quad x\in S_c.
\end{array}                                             \tag{6.2}
\]

Then

\[
                         A_h=\{x:h\in Z_x\}            \tag{6.3}
\]

realizes all selected targets and all owners.  It is enough to require the
owner net and, for every positive incidence \((c,x)\), one protected anchor

\[
 p_{c,x}\in I_c\cap R_x
 \quad\text{which lies in no selected interval whose target omits }x.
                                                               \tag{6.4}
\]

The owner net may similarly be certified by one protected anchor in every
owner supplier interval, but every such owner anchor must also lie in no
selected interval whose target omits \(x\).  Anchors may be reused without
limit.

#### Proof

The first assertion is the coordinatewise proof of Theorem 2.1; the
mandatory footprint makes every source letter nonempty.  Given anchors,
take \(Z_x\) to be their union together with the mandatory footprint
positions.  Every positive and owner interval is hit.  No
negative selected interval contains an anchor, and aperture compatibility
prevents it from containing a mandatory footprint of \(x\).  Hence every
negative cell remains disjoint from \(Z_x\). \(\square\)

This is a genuine separated-family statement: positive obligations and
owner obligations are separated from the entire negative interval family
by occurrence points.  Unlike pairwise separation of cell supports, it
allows a dense triangular collection of overlapping \(q\)-cells.

### Corollary 6.2 (bounded lower-compiler defect)

Let \({\cal L}\) be the strict-lower target family.  Suppose there is a set
\(D\subseteq{\cal L}\), \(|D|\le C\), and an injection

\[
             \psi:{\cal L}\setminus D\longrightarrow
             \{(j,q):1\le q\le d\}                   \tag{6.5}
\]

such that every assigned pair satisfies the individual aperture condition
and the retained assignments admit protected occurrence sets as in Theorem
6.1.  Then one depth-\(d\) factor realizes every strict-lower target outside
\(D\).  Its literal lower-compiler deficiency is at most \(C\).

Consequently, in any upper-complete construction to which the standard
bounded-literal-deficiency terminal repair applies, these pins contribute
at most \(C\) extra literal cells.  In particular, a uniform constant \(C\)
here is exactly strong enough for the lower side of a
\(B(k)+O(1)\) theorem.

The corollary does not claim that such an assignment or carrier exists.
It isolates the exact object that must be constructed: an almost-complete
target-to-cell matching carrying a protected interval-transversal on every
coordinate.

### Corollary 6.3 (separated block composition)

Suppose several locally realizing pin families are supported on cyclic arcs
\(B_1,\ldots,B_m\), and every owner window of length \(d+1\) meets at most
one \(B_a\).  If each local factor equals the maximal erosion factor outside
its own support arc, then all local pin families compose simultaneously.

#### Proof

For each coordinate and owner, at most one local modification can delete an
erosion supplier from its source window.  The one-block realization already
retains a supplier.  Cell equations are internal to their support blocks,
so the modifications do not interfere.  Equivalently, the union of their
negative interval families cannot create a new cover chain across two
blocks inside one required owner interval. \(\square\)

This recovers the earlier separated-position theorem, but permits an
arbitrarily dense family of overlapping cell pins inside each protected
block.

## 7. Cyclic boundary audit

The proof uses no hidden linear opening.

1. **Cells crossing (W-1\mid0).**  Every cell has length at most
   \(d<W\), hence a unique forward cyclic arc.  Definitions (0.5), (2.1),
   and all hitting conditions are rotation invariant.

2. **Runs crossing (W-1\mid0).**  Every coordinate has a negative owner,
   so each positive run is a proper arc.  Cut the coordinate's own circle at
   any negative owner and lift that run.  Lemmas 1.1--1.2 and Theorem 3.1
   are independent of this coordinate-specific cut.

3. **A cell meeting two runs.**  This cannot occur for (q\le d\), by
   Lemma 1.1.  Thus every positive-cell aperture has one linear lift.

4. **First and last erosion suppliers.**  They are the lagged arrival and
   current departure respectively.  Condition (K_c\subseteq S_c\) protects
   them even for a cell which crosses the displayed cyclic boundary.

5. **Last-to-first owner window.**  In a lift of its positive run it is just
   one of the intervals (1.4).  If clipped, it contains a protected erosion
   endpoint; if un-clipped, it is a full block of (d+1) positions.  Hence
   (0.9) has no missing wraparound exception.

6. **Minimum positive runs.**  Their erosion interval has one position.
   That position is both protected endpoints, so no aperture-compatible
   negative cell can delete it.  The labelled singleton gate is therefore
   preserved automatically by any simultaneous assignment satisfying
   (0.3).

## 8. Exact remaining mathematical gate

The mandatory-collar theorem gave an individually realizable edge relation

\[
                         K_c\subseteq S\subseteq E_c. \tag{8.1}
\]

Theorem 2.1 identifies the complete correction needed to pass from
individual edges to a simultaneous compiler:

\[
 \boxed{
 \begin{gathered}
 \text{choose a distinct target-to-cell matching, and for each coordinate}\\
 \text{prevent its zero-labelled cell intervals from covering either}\\
 \text{a positive target aperture or (d+1) consecutive erosion positions.}
 \end{gathered}}                                       \tag{8.2}
\]

There is no additional factorization obstruction after (8.2).  Equally,
there is no generic matroid shortcut: the exact residual object is a
matching constrained by an interval-cover clutter.

A proof of \(B(k)+O(1)\) through this route may therefore target the
following precise theorem.

> **Protected interval-transversal assignment.**  For every sufficiently
> large (k), construct the required owner/coatom carrier and inject all but
> (O(1)) strict-lower targets into distinct aperture-compatible cells so
> that every positive target-coordinate incidence and every owner-coordinate
> incidence has a protected occurrence anchor outside all negative assigned
> cell intervals of that coordinate.

Corollary 6.2 then closes the lower compiler with bounded defect.  Upper
coverage, residence, topology, and regeneration remain separate gates; no
claim about them is made here.
