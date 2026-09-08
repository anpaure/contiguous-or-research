# Ordinary promotion frames: pair-projection odd cuts are subcritical

Date: 2026-07-27

Scope: the unseeded ordinary-frame near-resolution hypergraph.  This is
a purely combinatorial statement.

## 0. Result

Put

\[
 n=2m,\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad N=\binom{2m}{M},
\]

and let an ordinary frame consist of one rank-\(M\) top and the \(M\)
cyclic rank-\(m\) windows in a directed cyclic order of that top.  Write

\[
 R=(M-1)!,\qquad
 D=\binom mH m!H!,\qquad
 \lambda={D\over R}={MN\over W}\le 1.
\tag{0.1}
\]

Weighting every frame representation by \(1/R\) loads every top by one
and every middle owner by \(\lambda\).

This note proves that a macroscopic obstruction cannot be obtained by
resolving these columns into domino pairs and then using graph odd-set
inequalities.  More precisely, every saturated owner-pair resolution of
the uniform fractional point produces a graph on exactly \(2W/M\)
owners with a fractional perfect matching whose largest edge weight is
at most \(2/m^2\).  Its matching deficiency is consequently at most

\[
                         {2W\over Mm^2}=O(W/m^3).
\tag{0.2}
\]

Thus such an odd cut can force at most \(O(W/m^3)\) missing frames, or
\(O(W/m^2)=o(W)\) additional missing middle owners.  The familiar
determinant-two triangle and the exact domino-twin residual evade this
conclusion only because their normalized pair weights are respectively
\(1/2\) and \(1\), rather than \(O(m^{-2})\).

This is a no-go for the whole pair-resolved odd-cycle lane, not a
near-resolution theorem.  A surviving obstruction must use physical
collisions outside the charged pairs or a genuinely higher-order
projection.

## 1. A capped fractional perfect matching has small odd deficiency

### Theorem 1.1 (capped Tutte--Berge lemma)

Let \(G=(S,E)\) be a finite simple graph.  Suppose that numbers
\(y_e\ge0\) satisfy

\[
 \sum_{e\ni v}y_e=1\quad(v\in S),
 \qquad
 \max_{e\in E}y_e\le\rho\le1.
\tag{1.1}
\]

Then

\[
 |S|-2\nu(G)\le \rho |S|,
 \qquad
 \nu(G)\ge{(1-\rho)|S|\over2}.
\tag{1.2}
\]

#### Proof

Fix \(A\subseteq S\), and consider an odd component \(C\) of
\(G-A\), of order \(c\).  There are no edges from \(C\) to another
component of \(G-A\), so (1.1) gives

\[
 y(C,A)=c-2y(E(C)).
\tag{1.3}
\]

If \(c\le1/\rho\), then

\[
 y(C,A)
 \ge c-\rho c(c-1)
 =1+(c-1)(1-\rho c)
 \ge1.
\tag{1.4}
\]

The boundary edges of distinct components are disjoint on their
\(S\setminus A\) endpoint.  Hence the sum of their \(y\)-weights is at
most

\[
 \sum_{a\in A}\sum_{e\ni a}y_e=|A|.
\tag{1.5}
\]

It follows that at most \(|A|\) odd components have order at most
\(1/\rho\).  Every remaining odd component has more than \(1/\rho\)
vertices, so there are at most \(\rho|S|\) of them.  Therefore

\[
 q(G-A)-|A|\le\rho|S|,
\tag{1.6}
\]

where \(q(G-A)\) denotes the number of odd components.  The
Tutte--Berge formula

\[
 |S|-2\nu(G)=\max_{A\subseteq S}\bigl(q(G-A)-|A|\bigr)
\tag{1.7}
\]

now proves (1.2). \(\square\)

The proof also gives the useful structural interpretation: a closed odd
component supporting (1.1) has more than \(1/\rho\) vertices unless it
spends at least one full unit of fractional mass across the Tutte cut.

## 2. Exact pair resolution of ordinary frame columns

Let \({\cal F}\) denote all ordinary frame representations, so
\(|{\cal F}|=NR\).  For a set \(S\) of middle owners, a **saturated
pair resolution** consists of coefficients

\[
 \theta_{F,p}\ge0
 \quad
 (F\in{\cal F},\ p\in\tbinom S2,\ p\subseteq F),
\tag{2.1}
\]

such that

\[
 \sum_{p\subseteq F}\theta_{F,p}=1\quad(F\in{\cal F})
\tag{2.2}
\]

and every charged owner receives its full uniform owner load:

\[
 {1\over R}
 \sum_{F\ni v}\ \,\sum_{p\ni v}\theta_{F,p}
 =\lambda
 \quad(v\in S).
\tag{2.3}
\]

This formulation includes the literal case in which every frame is
assigned one distinguished owner pair.  Allowing fractional
\(\theta\)'s only strengthens a proposed pair-cut certificate.

Summing (2.3) over \(v\), and using (2.2), gives the forced size

\[
 \lambda|S|
 ={2|{\cal F}|\over R}=2N,
 \qquad
 |S|={2N\over\lambda}={2W\over M}.
\tag{2.4}
\]

Define

\[
 y_p={1\over\lambda R}\sum_{F\in{\cal F}}\theta_{F,p}.
\tag{2.5}
\]

Equation (2.3) says exactly that \(y\) is a fractional perfect matching
on its support graph \(G\) on \(S\).

For distinct middle owners \(X,Y\), the exact ordinary-frame
pair-codegree table has maximum

\[
                         d(X,Y)\le {2D\over m^2}.
\tag{2.6}
\]

Since \(0\le\theta_{F,p}\le1\) and \(\lambda R=D\), (2.5)--(2.6)
give

\[
                         y_p\le {d(p)\over D}\le{2\over m^2}.
\tag{2.7}
\]

Applying Theorem 1.1 with \(\rho=2/m^2\), followed by (2.4), yields

\[
 \nu(G)
 \ge {W\over M}-{2W\over Mm^2}.
\tag{2.8}
\]

The target number of ordinary frames is \(N=\lambda W/M\le W/M\).
Consequently the deficit that this graph odd cut can place below the
target is bounded by

\[
 (N-\nu(G))_+
 \le {2W\over Mm^2}=O(W/m^3).
\tag{2.9}
\]

Multiplication by the \(M\) middle owners in one frame proves the
additional owner-loss bound \(2W/m^2=o(W)\).

Notice what (2.8) does and does not say.  A physical frame matching maps
to a matching of its distinguished charged pairs, so graph odd-set
inequalities can be used as upper-bound certificates.  Equation (2.8)
says that every such certificate has essentially enough capacity.  It
does not lift a graph matching back to pairwise disjoint physical frames;
collisions in the uncharged owners and tops remain outside this theorem.

## 3. Subcatalogue version

The same argument is independent of the factorial degree formula.  Let
\({\cal K}\) be any literal frame subcatalogue with an exact uniform
fractional point on a charged owner set \(S\), and suppose a saturated
pair resolution exists.  If its charged owner degree is \(d\) and

\[
 \max_{X\ne Y}d_{\cal K}(X,Y)\le\rho d,
\tag{3.1}
\]

then its projected graph odd deficiency is at most \(\rho|S|\).
Therefore a union of bounded odd triangles or domino cycles can have a
linear integral deficit only by violating (3.1): some charged pair must
carry a positive fraction of an owner degree.  At the ordinary physical
scale \(\rho=2/m^2\), pair-resolved odd components contribute only a
vanishing deficit.

This rules out the requested macroscopic domino/odd-cycle obstruction
under comparable degree--codegree geometry.  It leaves open, precisely,
a higher-order Hall obstruction or an exterior physical-collision
obstruction that cannot be represented by one saturated owner pair per
column.
