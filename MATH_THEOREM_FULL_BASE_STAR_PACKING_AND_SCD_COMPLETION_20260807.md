# Full hinge-base stars pack almost all of the bottom row and complete abstractly by one SCD

**Date:** 2026-08-07  
**Method:** maximal capacitated star packing followed by deterministic
symmetric-chain completion  
**Status:** theorem.  It strengthens the earlier low-base packing from
`MATH_THEOREM_SINGLE_BULGE_BASE_LAYER_INTEGRAL_STAR_PACKING_20260807.md`
to the complete base inventory of every saturated hinge ring, and removes
all higher-row integrality from the *abstract* completed-chain factor.  It
does not identify those SCD completions with the literal marked/bridge
chains of the hinge source.

## 1. The complete base inventory of one hinge ring

Use the odd triangular parameters

\[
 n=2m+1,\qquad s=m-2d,
\tag{1.1}
\]

and assume

\[
 d\ge2,\qquad s\ge1,\qquad n-s+1\ge4d.
\tag{1.2}
\]

Put

\[
                         Q=3d.
\tag{1.3}
\]

In the literal length-\(3d\) single-bulge ring of
`MATH_THEOREM_SINGLE_BULGE_TRIANGULAR_RESET_FACTOR_20260807.md`, write

\[
 P=C_0\setminus H,\qquad |P|=s-1,
\tag{1.4}
\]

and let \(F\) be its cyclic private-label set, \(|F|=3d\).  The schedule
is

\[
                         \mathsf L^{d-1}\mathsf H
\tag{1.5}
\]

repeated three times.

The earlier base-layer note counted only the marked rank-\(s\) targets at
the low phases.  After the exact bridge completion, there is in fact one
rank-\(s\) base at **every** phase:

\[
                         \boxed{\{P\cup\{f\}:f\in F\}}.
\tag{1.6}
\]

At a low phase this is the first marked target in (2.6) of the cited
hinge theorem.  At a high phase it is the first bridge target in (2.9).
Thus the saturated chain bank of one ring has a complete \(Q\)-petal
rank-\(s\) star, not merely the \(3(d-1)\)-petal low substar.

### Lemma 1.1 (every full base star lifts to a literal hinge ring)

Let

\[
 P\in{[n]\choose s-1},\qquad
 F\subseteq[n]\setminus P,\qquad |F|=3d.
\tag{1.7}
\]

Under (1.2), the star (1.6) is the complete base inventory of a literal
single-bulge ring.

#### Proof

There are

\[
 |[n]\setminus P|=n-s+1
\]

coordinates outside \(P\).  After reserving \(F\), condition (1.2) leaves
at least \(d\) coordinates.  Choose a \(d\)-set

\[
                         H\subseteq[n]\setminus(P\cup F)
\]

and put \(C_0=P\cup H\).  Designate any three members of \(F\) as the
high phases, arrange the other \(3(d-1)\) members in the three low runs,
and use (1.5).  The literal hinge theorem supplies the owner row,
palettes, residence and the saturated bridge completion.  Its rank-\(s\)
bases are exactly (1.6). \(\square\)

Notice that the reset banks \(H\) of different rings need not be disjoint
for this lemma.  Only named target disjointness is asserted below.

## 2. Almost-spanning integral packing of full base stars

Let

\[
 \mathcal V={ [n]\choose s},\qquad
 \mathcal C={ [n]\choose s-1},
 \qquad V=|\mathcal V|,\quad C=|\mathcal C|,
\tag{2.1}
\]

and put

\[
                         v=n-s+1.
\tag{2.2}
\]

Every centre in \(\mathcal C\) has \(v\) rank-\(s\) supersets, every
target in \(\mathcal V\) contains \(s\) centres, and hence

\[
                         Cv=Vs.
\tag{2.3}
\]

Greedily choose a previously unused centre with at least \(Q\) unused
rank-\(s\) supersets, reserve any \(Q\) of them as one star, and mark the
targets used.  Stop when no such centre remains.

### Theorem 2.1 (full-base integral star packing)

If \(M\) stars and \(U=MQ\) rank-\(s\) targets are selected, then

\[
 \boxed{
 M\ge {C(v-Q+1)\over Qs+v-Q+1}}
\tag{2.4}
\]

and

\[
 \boxed{
 {U\over V}
 \ge
 {Qs(v-Q+1)\over v(Qs+v-Q+1)}.}
\tag{2.5}
\]

In the triangular regime \(d=\Theta(\sqrt n)\), this is

\[
                         {U\over V}=1-O(1/d).
\tag{2.6}
\]

Every selected star lifts, by Lemma 1.1, to a literal hinge ring whose
**entire** saturated rank-\(s\) base inventory is disjoint from that of
every other selected ring.

#### Proof

At termination every unselected centre has at most \(Q-1\) unused
supersets, hence at least \(v-Q+1\) used supersets.  Counting incidences
between unselected centres and used targets gives

\[
                         (C-M)(v-Q+1)\le U s=MQs.
\tag{2.7}
\]

Rearranging proves (2.4).  Multiply by \(Q\), divide by \(V\), and use
(2.3) to obtain (2.5).

Here \(Q=\Theta(d)\), \(s,v=\Theta(n)\), and \(Qs\gg v\).  The two
losses in (2.5) are

\[
 O(Q/v)+O(v/(Qs))=O(1/d),
\]

which proves (2.6).  The lifting assertion is Lemma 1.1. \(\square\)

The replacement of \(3(d-1)\) by \(3d\) is not merely a harmless
constant change: it means no high-phase base remains outside the packed
inventory.

## 3. One SCD completes all selected bases simultaneously

Fix once and for all a symmetric-chain decomposition \(\mathscr D\) of
the Boolean lattice \(B_n\).  Every rank-\(s\) set belongs to one unique
chain of \(\mathscr D\), and every such chain reaches rank at least
\(n-s>m-1\).

For \(S\in{[n]\choose s}\), write

\[
 S=S_s\subset S_{s+1}\subset\cdots\subset S_{m-1}
\tag{3.1}
\]

for the segment of its unique SCD chain.

### Theorem 3.1 (deterministic abstract completion)

Let \(\mathcal U\subseteq{[n]\choose s}\) be any family of distinct
rank-\(s\) sets.  Then the chain segments (3.1), over
\(S\in\mathcal U\), are pairwise target-disjoint and contain exactly one
target at every rank

\[
                         s,s+1,\ldots,m-1.
\tag{3.2}
\]

Consequently, applying this construction to the full-base star packing
of Theorem 2.1 gives \(U\) pairwise disjoint saturated lower chains.  They
may be grouped back into the selected \(3d\)-tuples, one tuple for each
literal hinge ring.

#### Proof

Different rank-\(s\) sets lie in different SCD chains, because an
inclusion chain contains at most one set of any fixed rank.  Distinct SCD
chains are disjoint.  Each selected chain contains every rank in (3.2),
which proves the claim. \(\square\)

### Corollary 3.2 (all higher completed-chain rows are integrally exact)

For every \(j=0,1,\ldots,2d-1\), the selected abstract factor contains
exactly \(U\) distinct targets of rank \(s+j\).  Thus no separate
matching, rounding, or divisibility theorem is needed for any completed
lower row once the full base star packing is fixed.

For a ring with endpoint ages

\[
                         0,1,\ldots,d-1
\]

repeated three times, the appropriate ranks of each saturated SCD chain
can be designated as the marked hinge profile (2.2)--(2.3), with the
complementary ranks designated as bridges.  This produces the same
rank-multiplicity ledger as the literal hinge theorem, now with global
target disjointness.

## 4. Exact quantifier boundary

Theorems 2.1 and 3.1 prove the following joint statement:

> There is an almost-spanning integral packing of complete \(3d\)-base
> hinge stars, and those exact bases admit a deterministic, globally
> target-disjoint saturated-chain completion through every strict-lower
> rank.

They do **not** prove that the SCD chain above \(P\cup\{f\}\) is the
literal marked-and-bridge chain forced by the source word of Lemma 1.1.
The two constructions currently share their rank-\(s\) bases, but not
necessarily their higher named targets.

This distinction is essential.  The literal hinge ring couples its
\(3d\) endpoint chains through one common reset bank \(H\), one cyclic
private order, and the phase schedule.  An arbitrary SCD completion makes
independent choices above the bases and need not respect that coupling.

Accordingly the surviving lower-side theorem is no longer an all-row
capacity or integrality statement.  It is the following alignment
statement.

> **Literal SCD-alignment problem.**  Choose the full-base star packing,
> reset banks and cyclic private orders so that the literal completed
> chains of the selected hinge rings form a subfamily of one global chain
> decomposition (or, equivalently for the application, are pairwise
> target-disjoint).

After this alignment, the remaining independent gates are owner/upper
compatibility, cycle fusion and the terminal compiler.  Without it, the
abstract completion cannot be substituted into the literal source word.

## 5. Audit of the preceding base-layer theorem

The proof of
`MATH_THEOREM_SINGLE_BULGE_BASE_LAYER_INTEGRAL_STAR_PACKING_20260807.md`
is correct in its stated scope.  In particular:

1. its outside-coordinate count is
   \(|[n]\setminus P|=n-s+1=v\);
2. after reserving \(3(d-1)\) low labels, condition \(v\ge4d\) leaves
   the required \(d+3\) reset/high labels;
3. at termination, every unselected centre is incident with at least
   \(v-R+1\) used targets;
4. the incidence inequality
   \((C-M)(v-R+1)\le MRs\) and its normalized consequence are exact.

Its only limitation is deliberate scope: it omits the three high-phase
bases because they arise in the bridge bank rather than the marked-low
bank.  The present theorem incorporates them by taking \(Q=3d\), with the
same asymptotic packing guarantee.

## 6. Verdict

The correlated higher rows are no longer an abstract integral-packing
obstruction.  Once all \(3d\) bases of each ring are packed, one fixed SCD
completes every selected chain simultaneously and without collisions.

The exact remaining lower obstruction is sharper:

\[
 \boxed{\text{make the literal hinge completions agree with a globally
 disjoint chain completion.}}
\]

That is an alignment problem, not a rank-count, Hall, divisibility, or
row-by-row rounding problem.
