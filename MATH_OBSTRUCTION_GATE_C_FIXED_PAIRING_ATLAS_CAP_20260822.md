# Gate C: the universal fixed-pairing atlas cap

**Status (2026-08-22).**  Every assertion below is proved.  A coherent FIFO
tour built from one fixed perfect coordinate pairing has all of its internal
middle targets in a stratum of exact size

\[
                         b(b-1)2^{b-2}.                 \tag{0.1}
\]

Consequently a rankwise-target-disjoint family of full such tours has at
most `2^(b-2)` members.  The same conclusion, up to a factor `1+o(1)`,
holds after arbitrary `o(q)` thinning of every tour.  Since a central flag
factor needs `Theta(4^b/b^(5/2))` near-full tours, any successful Gate-C
construction must use

\[
                         \Omega(2^b/b^{5/2})             \tag{0.2}
\]

genuinely different perfect pairings.  In particular no corrected
antipodal block-shuffle family—equal, unequal, or multiscale—can close the
packing gate while its pairing is fixed.

Throughout, `b>=3` is odd, `Omega` has size `2b`,

\[
 q=b(b-1),\qquad W={2b\choose b},\qquad
 N={2b\choose b-1}={b\over b+1}W.                     \tag{0.3}
\]

Here `N` is the number of central flags in a full symmetric-chain factor.

## 1. The defect-one stratum of a pairing

Fix a perfect pairing

\[
                         \mathcal P=\{P_0,\ldots,P_{b-1}\}          \tag{1.1}
\]

of `Omega`.  Call a middle set `C in binom(Omega,b)` *defect one relative
to `P`* if exactly one pair is empty, exactly one different pair is
doubled, and every remaining pair is split.  Let `V_P^(1)` be this stratum.

### Lemma 1.1 (exact atlas size)

\[
                         |\mathcal V_{\mathcal P}^{(1)}|
                         =b(b-1)2^{b-2}.                \tag{1.2}
\]

#### Proof

Choose the empty pair in `b` ways and the different doubled pair in `b-1`
ways.  From each of the other `b-2` pairs choose either member.  The empty
and doubled pairs are recoverable from the resulting set, so no two choices
have been counted together. \(\square\)

## 2. Every fixed-pairing tour lies in this atlas

A coherent FIFO tour on `P` has `b` packets.  At the packet with special
pair `P_t`, each of its `b-1` internal middle windows is indexed by the
different pair `P_i` currently crossing the FIFO boundary.  The window
omits `P_t`, contains both members of `P_i`, and contains one member of
every other pair.  Denote it by `T_(t,i)`.

### Lemma 2.1 (distinct internal targets)

The `q=b(b-1)` targets `T_(t,i)`, `t!=i`, are distinct members of
`V_P^(1)`.

#### Proof

The empty and doubled pairs of `T_(t,i)` are respectively `P_t` and `P_i`.
Thus the ordered index `(t,i)` is recoverable from the target itself.
Distinct ordered indices give distinct targets, and the preceding packet
description proves membership in `V_P^(1)`. \(\square\)

This conclusion is independent of the cyclic order of the pairs, the
initial transversal state, and the within-pair labels.  It is therefore
valid for every coherent tour whose underlying pairing is `P`.

## 3. Exact matching cap and thinning robustness

### Theorem 3.1 (one-pairing cap)

Let `C` be a collection of coherent tours with the same pairing `P`.  From
each tour `E`, retain a set `R_E` of its internal flags, and suppose all
retained middle targets are distinct between different tours.  If

\[
                         |R_E|\ge(1-\varepsilon)q       \tag{3.1}
\]

for every `E`, where `0<=epsilon<1`, then

\[
                         |\mathcal C|
                         \le {2^{b-2}\over1-\varepsilon}.          \tag{3.2}
\]

In particular, a rankwise-target-disjoint family of full tours has at most
`2^(b-2)` members.

#### Proof

Lemma 2.1 puts every retained middle target in `V_P^(1)`.  It also says
that the retained targets within one tour are distinct.  The hypothesis
makes them distinct between tours as well.  Hence

\[
 (1-\varepsilon)q|\mathcal C|
 \le\sum_{E\in\mathcal C}|R_E|
 \le|\mathcal V_{\mathcal P}^{(1)}|
 =q2^{b-2}.
\]

Cancel `q` to obtain (3.2). \(\square\)

The same count handles a menu of pairings.

### Corollary 3.2 (pairing-diversity lower bound)

Suppose a rankwise-target-disjoint family of `m` thinned coherent tours
uses at most `R` underlying pairings and retains at least
`(1-epsilon)q` flags per tour.  Then

\[
                         m\le {R2^{b-2}\over1-\varepsilon}.        \tag{3.3}
\]

Consequently, covering `(1-o(1))N` flags of a central factor by tours with
`q-o(q)` retained flags requires

\[
 R\ge(1-o(1)){N\over q2^{b-2}}
   =\Theta\left({2^b\over b^{5/2}}\right).              \tag{3.4}
\]

#### Proof

The union of the `R` defect-one strata has size at most
`Rq2^(b-2)`, whether or not the strata overlap.  The proof of Theorem 3.1
then gives (3.3).  A cover of `(1-o(1))N` flags uses at least
`m>=(1-o(1))N/q` tours.  Combining this with (3.3) proves the first
expression in (3.4).  Finally

\[
 N={b\over b+1}{2b\choose b}
   =(1+o(1)){4^b\over\sqrt{\pi b}},\qquad q=(1+o(1))b^2,
\]

which gives the displayed order. \(\square\)

## 4. Consequence for block constructions

A corrected antipodal lift has the form

\[
 \pi(x)=\alpha(x)+b\epsilon_x,\qquad
 \pi(x+b)=\pi(x)+b\pmod {2b}.                          \tag{4.1}
\]

It maps every canonical pair `{x,x+b}` to the canonical pair
`{alpha(x),alpha(x)+b}`.  Thus all equal-block, unequal-block, and recursive
block shuffles using (4.1) preserve the same perfect pairing.  Their
factor intersections may have factorially many labels and may individually
retain `q-o(q)` flags, but Theorem 3.1 bounds every rankwise-disjoint
near-full subfamily by `2^{b+o(b)}` members.  This is exponentially below
the `Theta(4^b/b^(5/2))` required by one central factor.

This obstruction does not rule out block ideas whose outer layer moves the
perfect pairing, nor the full all-pairing coherent-tour orbit.  It says
that pairing diversity is an exponential resource, not a polynomial-size
cleanup that can be added after a fixed-pairing construction.

The companion checker
`scratch/verify_gate_c_fixed_pairing_atlas_cap_20260822.py` enumerates the
canonical fixed-pairing tours for small odd `b`, verifies distinctness and
the exact defect-one atlas, and checks the finite identities above.
