# Mesoscopic cyclic intervals: exact orbit endpoint splicing

Date: 2026-07-25

Pure mathematics only.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom nm,
\]

and let \(H=o(m)\).  The rotor/SCD two-resolution orbit does admit an
exact endpoint-splicing theorem at the level of genuine cyclic orders.
After lifting a rotor state to a pointed oriented cyclic order, the legal
rigid successor is the deterministic one-step rotation.  In the complete
coordinate orbit, the starts and ends of any prescribed family of rigid
runs are uniform on exact pointed-order types.  They can therefore be
spliced integrally, using only rigid rotation edges.

The resulting exact identity is

\[
 \boxed{R_{\rm orb}^{\min}=n!\,p_* ,}
\tag{0.1}
\]

where \(p_*\) is the minimum number of cyclic-order runs in one admissible
coverage color.  Thus orbit symmetry loses nothing, but it also gains
nothing over the best single color.

For a decorated SCD color, all central-band masks are covered with zero
holes.  Hence a single color covering all but \(o(W)\) band masks with
\(o(W)\) run starts exists precisely when the corresponding one-color
minimum satisfies

\[
 p_*=o(W).
\tag{0.2}
\]

This conclusion is strictly weaker than the Mesoscopic Cyclic-Interval
Near-Design theorem.  A genuine near-design of full cyclic orders requires

\[
 p_*=(1+o(1)){W\over n},
\tag{0.3}
\]

not merely \(p_*=o(W)\).  For the literal segmented interval compiler,
whose excess is \((2H+1)p_*\), coefficient one requires

\[
 Hp_*=o(W).
\tag{0.4}
\]

Neither (0.2), (0.3), nor (0.4) follows from the two-resolution identity.
The exact unresolved object is one decorated coverage color with the
corresponding rigid-run bound.  Allowing the more general rotor successor
used in the flexible endpoint-transport theorem proves a weaker path-cover
statement and cannot be substituted for a cyclic-interval proof.

## 1. Pointed cyclic orders and their runs

Let \(\Omega\) be the set of pointed oriented cyclic orders on \([n]\).
We write an element as a linear word

\[
 \omega=(x_0,x_1,\ldots,x_{n-1}),
\]

where all \(x_i\) are distinct.  Thus \(|\Omega|=n!\).  Let

\[
 \rho\omega=(x_1,x_2,\ldots,x_{n-1},x_0)
\tag{1.1}
\]

be the rigid rotation successor.  The symmetric group
\(G=S_n\) acts on labels, commutes with \(\rho\), and acts freely and
transitively on \(\Omega\).

For \(1\le r\le n-1\), put

\[
 I_\omega(r)=\{x_0,\ldots,x_{r-1}\}.
\tag{1.2}
\]

The band flag exposed at \(\omega\) is

\[
 {\cal F}_H(\omega)
 =\{I_\omega(r):m-H\le r\le m+H+1\}.
\tag{1.3}
\]

Let

\[
 {\cal T}_H
 =\bigcup_{r=m-H}^{m+H+1}\binom{[n]}r.
\tag{1.4}
\]

For \(C\subseteq\Omega\), define its band-hole count by

\[
 h_H(C)
 =\left|{\cal T}_H\setminus
        \bigcup_{\omega\in C}{\cal F}_H(\omega)\right|.
\tag{1.5}
\]

The \(\rho\)-orbits in \(\Omega\) are the unpointed oriented cyclic
orders, each with exactly \(n\) points.  The induced directed graph
\(\rho[C]\) is a disjoint union of directed paths and whole directed
cycles.  Define \(p(C)\) to be its number of components, counting a whole
cycle once.  Equivalently,

\[
 p(C)
 =
 \sum_{O\in\Omega/\langle\rho\rangle}
 \begin{cases}
  0,&C\cap O=\varnothing,\\
  1,&C\cap O=O,\\
  |\{\omega\in C\cap O:\rho^{-1}\omega\notin C\}|,
     &\text{otherwise}.
 \end{cases}
\tag{1.6}
\]

Thus \(p(C)\) is exactly the least number of genuine cyclic-order
intervals whose disjoint union as pointed occurrences is \(C\).

## 2. The exact two-resolution orbit

Fix any \(C\subseteq\Omega\), with \(|C|=s\), and retain indexed
occurrences in

\[
 \widehat C=\bigsqcup_{g\in G}gC.
\tag{2.1}
\]

Call \(g\) the coverage color of the occurrences in \(gC\).

### Lemma 2.1 (universal pointed-order orbit)

Every \(\omega\in\Omega\) occurs exactly \(s\) times in \(\widehat C\).
Consequently \(\widehat C\) has the two exact resolutions

\[
 \boxed{
 \widehat C
 =\bigsqcup_{g\in G}gC
 =s\bigsqcup_{O\in\Omega/\langle\rho\rangle}O.}
\tag{2.2}
\]

The first is the coverage resolution; the second is a resolution into
genuine rigid cyclic-order cycles.

#### Proof

Fix \(c\in C\) and \(\omega\in\Omega\).  Freeness and transitivity give a
unique \(g\in G\) with \(gc=\omega\).  Summing over the \(s\) indexed
members of \(C\) proves that \(\omega\) has multiplicity \(s\).
Partitioning \(\Omega\) into its \(\rho\)-orbits proves (2.2).
\(\square\)

This is the cyclic-interval version of the rotor/SCD two-resolution
identity.  It already has integral multiplicities on both sides.

## 3. Strongest exact rigid low-switch lemma

A **rigid successor resolution** of \(\widehat C\) pairs every occurrence
of type \(\omega\) with one occurrence of type \(\rho\omega\).  Since the
two type multiplicities agree, such resolutions exist and are disjoint
unions of directed cycles.  Split their cyclic color words into maximal
constant-color runs; a monochromatic whole cycle counts as one run.

### Theorem 3.1 (rigid orbit endpoint-splicing identity)

Among all rigid successor resolutions of \(\widehat C\), while color
\(g\) retains precisely the pointed states \(gC\), the minimum total
number of monochromatic runs is

\[
 \boxed{R_{\rm orb}(C)=|G|p(C)=n!\,p(C).}
\tag{3.1}
\]

Moreover, there is an optimal resolution in which every color has exactly
\(p(C)\) runs.

#### Proof: lower bound

Fix a color \(g\).  A same-color successor edge leaving a state
\(\omega\in gC\) can only go to the unique type \(\rho\omega\), and that
type must also belong to \(gC\).  Therefore the same-color subgraph is a
subgraph of \(\rho[gC]\).  Its monochromatic components refine the
components of \(\rho[gC]\), so color \(g\) has at least

\[
 p(gC)=p(C)
\]

runs.  Summing over all \(n!\) colors proves

\[
 R\ge n!\,p(C).
\tag{3.2}
\]

#### Proof: upper bound

In every color \(g\), retain all internal edges of the path and cycle
components of \(\rho[gC]\).  Whole-cycle components are already closed.
Suppose the base set \(C\) has \(a\) open path components; it then has
\(a\) path starts and \(a\) path ends.

Fix an exact pointed order \(\omega\).  For each indexed base path end
\(b\), there is a unique \(g\) with \(gb=\omega\).  Hence exactly \(a\)
open color paths end at type \(\omega\) throughout the full orbit.
Similarly, exactly \(a\) open color paths start at type
\(\rho\omega\).

Pair these two \(a\)-element occurrence fibres arbitrarily and insert the
rigid edge

\[
 \omega\longrightarrow\rho\omega.
\tag{3.3}
\]

Do this independently for every \(\omega\).  Every open path receives one
predecessor and one successor, so all occurrences now lie on directed
rigid cycles.

No inserted edge is monochromatic.  Indeed, if an end \(\omega\) and a
start \(\rho\omega\) had the same color \(g\), then both types would lie
in \(gC\), and the edge between them would already join the two purported
components of the induced graph \(\rho[gC]\), a contradiction.  Thus the
inserted edges neither merge nor split any color run.  Every color has
exactly \(p(C)\) runs, proving the reverse inequality in (3.1).
\(\square\)

The proof is stronger than splicing through the regular flexible rotor
graph: every added edge is the deterministic rotation of one exact
pointed cyclic order.  Hence every completed physical cycle is a rigid
cyclic-order circuit, possibly making several indexed laps of the same
underlying order.

There is also no hidden circuit-cut charge.  Cut every nonmonochromatic
ambient cycle at an inserted cross-color edge; this does not split a
monochromatic run.  A wholly monochromatic ambient cycle is already one
full \(\rho\)-orbit and counts as one run after any cut.  Thus (3.1) is
also the exact number of physical linear run starts.

## 4. Quota-preserving recoloring

Let \(\mathfrak C\) be a nonempty \(G\)-invariant family of subsets of
\(\Omega\), all of the same size \(s\).  Its members are the admissible
coverage colors.  Define

\[
 p_*(\mathfrak C)=\min_{C\in\mathfrak C}p(C).
\tag{4.1}
\]

Start from the full orbit pool of any one \(C_0\in\mathfrak C\).  Allow a
recoloring into \(n!\) admissible colors, with exact pointed-order
multiplicities preserved, and optimize the rigid successor resolution as
well.

### Theorem 4.1 (exact quota optimum)

\[
 \boxed{
 R_{\rm orb}^{\mathfrak C}=n!\,p_*(\mathfrak C).}
\tag{4.2}
\]

If every \(C\in\mathfrak C\) has \(h_H(C)\le b\), the optimal resolution
may be chosen so that every one of its colors has at most \(b\) band
holes and exactly \(p_*(\mathfrak C)\) runs.

#### Proof

For the lower bound, each admissible color \(C_g\) contributes at least
\(p(C_g)\ge p_*(\mathfrak C)\) runs by the lower-bound proof of
Theorem 3.1.

For the upper bound, choose a minimizer \(C^*\).  Lemma 2.1 says that the
full orbit pools of \(C_0\) and \(C^*\) both contain exactly \(s\) copies
of every pointed-order type.  Repartition the pool, matching only equal
types, into the colors \(gC^*\).  Apply Theorem 3.1.  Every color is a
coordinate image of \(C^*\), so it has the same hole count and exactly
\(p_*(\mathfrak C)\) runs.
\(\square\)

Thus arbitrary orbit recoloring cannot average a large one-color run
functional away.  It succeeds at a given scale if and only if one
admissible integral atom already succeeds at that scale.

## 5. Decorated SCD colors

Let \({\cal D}\) be a full symmetric-chain decomposition of \(B_n\).  It
has exactly \(W\) chains.  For a chain

\[
 A_a\subset A_{a+1}\subset\cdots\subset A_{n-a},
 \qquad |A_r|=r,
\tag{5.1}
\]

write \(A_{r+1}=A_r\cup\{z_{r+1}\}\).  Choose an arbitrary order of
\(A_a\), then list

\[
 z_{a+1},z_{a+2},\ldots,z_{n-a},
\]

and finally choose an arbitrary order of
\([n]\setminus A_{n-a}\).  The resulting pointed cyclic order
\(\omega_A\) satisfies

\[
 I_{\omega_A}(r)=A_r
 \qquad(a\le r\le n-a).
\tag{5.2}
\]

Call this a full decoration.  More generally, a band decoration is allowed
to choose any pointed order satisfying (5.2) only for

\[
 \max\{a,m-H\}\le r\le\min\{n-a,m+H+1\}.
\tag{5.3}
\]

Choose one band decoration for every chain and put

\[
 C({\cal D})=\{\omega_A:A\text{ is a chain of }{\cal D}\}.
\tag{5.4}
\]

Distinct chains have distinct rank-\(m\) members, so the pointed orders in
\(C({\cal D})\) are distinct and

\[
 |C({\cal D})|=W.
\tag{5.5}
\]

Every band mask lies in one chain of \({\cal D}\), and by (5.3) it is a
prefix of that chain's decoration.  In particular,

\[
 \boxed{h_H(C({\cal D}))=0.}
\tag{5.6}
\]

Let \(\mathfrak C_H^{\rm SCD}\) be the family of all such band-decorated
SCD colors.  Full decorations show that this family is nonempty.  Put

\[
 p_H^{\rm SCD}
 =\min_{C\in\mathfrak C_H^{\rm SCD}}p(C).
\tag{5.7}
\]

### Corollary 5.1 (exact SCD-orbit low-switch gate)

The full pointed-order two-resolution orbit has an integral rigid
successor resolution into genuine SCD coverage colors with minimum total
run count

\[
 \boxed{n!\,p_H^{\rm SCD}.}
\tag{5.8}
\]

Every color in an optimal resolution covers every central-band mask.
Consequently a single exact-coverage color with \(o(W)\) rigid run starts
exists if and only if

\[
 p_H^{\rm SCD}=o(W).
\tag{5.9}
\]

This is the strongest conclusion supplied by orbit endpoint symmetry
alone.  The asymptotic assertion (5.9) remains unproved.

## 6. Exact segmented compiler

Let \(C\subseteq\Omega\) be decomposed into its \(p(C)\) rigid runs.  A
run of \(t\) consecutive phases of a cyclic order can expose every band
flag (1.3) belonging to those \(t\) phases using exactly

\[
 t+2H+1
\tag{6.1}
\]

entries.

Indeed, if its phases begin at \(j,j+1,\ldots,j+t-1\), emit the
length-\((m-H)\) intervals beginning at

\[
 j,j+1,\ldots,j+t+2H.
\tag{6.2}
\]

There are \(t+2H+1\) displayed entries.  A union of \(u\) consecutive
displayed entries beginning at phase \(i\) is the cyclic interval of length

\[
 m-H+u-1.
\tag{6.3}
\]

Thus the conservative uniform count (6.1) covers every rank in
\(m-H,\ldots,m+H+1\).

Summing over runs and then appending the holes literally gives:

### Proposition 6.1 (run/defect compilation)

\[
 \boxed{
 L_H(C)\le |C|+(2H+1)p(C)+h_H(C).}
\tag{6.4}
\]

For a decorated SCD color this becomes

\[
 L_H(C)\le W+(2H+1)p(C).
\tag{6.5}
\]

Therefore the coefficient-safe segmented target is

\[
 p(C)=o(W/H),
\tag{6.6}
\]

which is stronger than merely \(p(C)=o(W)\).

## 7. Relation to the Mesoscopic Cyclic-Interval Near-Design theorem

Every rigid run has at most \(n\) pointed states, so

\[
 \boxed{p(C)\ge {|C|\over n}.}
\tag{7.1}
\]

Conversely, extend every run of \(C\) to its whole \(\rho\)-cycle.  If
two runs lie on the same cycle, retain two indexed copies of that cyclic
order.  This gives a multiset \({\cal P}(C)\) of exactly \(p(C)\) cyclic
orders whose intervals cover every flag covered by \(C\).  Its completion
excess is

\[
 np(C)-|C|.
\tag{7.2}
\]

Hence, if

\[
 |C|=W+o(W),\qquad
 h_H(C)=o(W),\qquad
 p(C)=(1+o(1)){W\over n},
\tag{7.3}
\]

then \({\cal P}(C)\) is precisely a Mesoscopic Cyclic-Interval
Near-Design:

\[
 |{\cal P}(C)|=(1+o(1)){W\over n}
\]

and it misses only \(o(W)\) masks in the whole band.

Conversely, from any such near-design \({\cal P}\), take all pointed
phases of its indexed cyclic orders.  The resulting occurrence set has

\[
 |C|=n|{\cal P}|=W+o(W),\qquad
 p(C)=|{\cal P}|,\qquad
 h_H(C)=o(W).
\tag{7.4}
\]

Thus (7.3) is an exact run formulation of the near-design theorem.
Condition \(p(C)=o(W)\) gives only a segmented near-design with diverging
average run length.  It does not imply (7.3), because \(np(C)\) may be
much larger than \(W\).

## 8. Exact remaining discrepancy

The rotor/SCD two-resolution supplies both of the following integral
objects in the same complete orbit:

1. the dynamic resolution into rigid cyclic-order cycles, with the
   optimal scalar number \(W/n\) of cycles per \(W\) pointed states;
2. the coverage resolution into decorated SCD colors, each with zero
   band holes.

Theorems 3.1 and 4.1 completely solve endpoint completion between these
resolutions.  They reduce the low-switch problem to one atom:

\[
 \boxed{
 \min_{\substack{C\text{ admissible coverage color}}}
 p(C).}
\tag{8.1}
\]

There are three distinct thresholds.

\[
\begin{array}{c|c}
\text{desired conclusion}&\text{required one-color bound}\\ \hline
o(W)\text{ run starts}&p(C)=o(W),\\
W+o(W)\text{ segmented compiler}&Hp(C)=o(W),\\
\text{full-order mesoscopic near-design}
 &p(C)=(1+o(1))W/n.
\end{array}
\tag{8.2}
\]

Orbit symmetry proves the exact multiplier \(n!\) and permits rigid
endpoint splicing with no additional run.  It proves none of the three
one-color estimates in (8.2).  That is the exact remaining integral
discrepancy.

Finally, this rigid functional dominates the flexible rotor path-cover
functional.  A rigid rotation edge is a legal rotor edge after forgetting
the internal orders of the two large blocks, but not every legal rotor
edge is a rigid rotation edge for a fixed pointed order.  Therefore

\[
 p_{\rm rotor}(C)\le p(C),
\tag{8.3}
\]

and an arbitrary regular-rotor endpoint completion cannot be cited as a
proof of the cyclic-interval near-design theorem.
