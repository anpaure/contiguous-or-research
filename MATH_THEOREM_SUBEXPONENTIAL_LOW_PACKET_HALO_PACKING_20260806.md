# Subexponential low-target packets admit pairwise halo-disjoint planting

**Date:** 2026-08-06  
**Method:** stabilizer-orbit sampling and a first-moment collision bound; no
computation or search  
**Status:** unconditional abstract packing theorem.  Its PBBS consequence is
conditional only on producing one coordinate-covariant literal packet for
each low target.  It does not construct those packets or complete their
protected owner factor.

## 1. Scale separation

Let

\[
                         n=2m+1,
 \qquad d=O(\sqrt m),
\]

and let

\[
 \mathcal S_d=\{S\subseteq[n]:1\le |S|\le d\},
 \qquad L_d=|\mathcal S_d|.
\]

Then

\[
 \log L_d=O(d\log(n/d))=o(n),
 \qquad L_d=2^{o(n)}.                              \tag{1.1}
\]

By contrast every central layer has size

\[
 \binom n{m+O(d)}=2^{n-o(n)}.                     \tag{1.2}
\]

Thus even a polynomial-size protected packet for every member of
`mathcal S_d` uses only a subexponential number of resources.

## 2. Covariant packet families

Fix constants `C,A`.  For every `S in mathcal S_d`, suppose a packet
template `Pi_S` has at most

\[
                              p(n)\le n^A          \tag{2.1}
\]

named resources in its complete protected halo.  Every resource is a set
of one of the ranks

\[
                         m-Cd,\ldots,m+Cd.          \tag{2.2}
\]

Assume the following coordinate-covariant embedding property.

* The stabilizer `Sym([n]-S)` acts on the packet embeddings.
* For every named halo role `rho`, its value in a uniform embedding is
  uniform on one stabilizer orbit of central-rank sets.
* Every such orbit has size `2^(n-o(n))`, uniformly in `S` and `rho`.

The last condition is automatic, for example, when the role has fixed
intersection with `S` and its remaining `m+O(d)` labels are an otherwise
arbitrary subset of `[n]-S`.  Indeed its orbit then has size

\[
 \binom{n-|S|}{m+O(d)-O(d)}=2^{n-o(n)}.            \tag{2.3}
\]

No independence between the roles *inside one packet* is assumed.

## 3. Halo-disjoint packing

### Theorem 3.1

Under the hypotheses of Section 2, for all sufficiently large `n` one may
choose one embedding of every packet `Pi_S`, `S in mathcal S_d`, so that
the complete named halos of distinct packets are disjoint.

#### Proof

Choose the packet embeddings independently, one for each target.  Fix
distinct targets `S,T` and named roles `rho` of `Pi_S` and `sigma` of
`Pi_T`.  Condition on the complete embedding of `Pi_S`.  The value of
role `rho` is now one fixed set `U`.  The value of role `sigma` is uniform
on an orbit of size at least

\[
                              N_n=2^{n-o(n)}.
\]

It either cannot equal `U`, or does so with probability exactly `1/N_n`.
Consequently

\[
 \Pr\bigl(\rho(\Pi_S)=\sigma(\Pi_T)\bigr)
 \le 2^{-n+o(n)}.                                  \tag{3.1}
\]

There are at most

\[
                         L_d^2p(n)^2=2^{o(n)}      \tag{3.2}
\]

ordered choices of `(S,T,rho,sigma)`.  The union bound and (3.1) give

\[
 \Pr(\text{some cross-packet halo collision})
 \le 2^{-n+o(n)}<1.                                \tag{3.3}
\]

Hence a collision-free simultaneous choice exists.  \(\square\)

The proof also permits a prescribed `2^{o(n)}` forbidden halo: add its
elements as deterministic roles in (3.2).

## 4. Consequence for low-target repair architecture

Suppose every `S in mathcal S_d` has one literal source packet with all of
the following properties.

1. It contains a source interval of width at most `d` and OR value `S`.
2. It uses `poly(n)` owner, immediate-palette, residence, upper-witness,
   and source-history resources.
3. All those resources form a coordinate-covariant halo satisfying
   Section 2.
4. The selected phase of the packet is a degree-at-most-two protected
   incidence forest.

Then Theorem 3.1 plants one occurrence for **every** low target with no
cross-packet resource collision.  The resulting total protected bank has

\[
                  O\bigl(p(n)L_d\bigr)=2^{o(n)}     \tag{4.1}
\]

resources, which is negligible compared with the middle-layer size
`2^(n-o(n))`.

Thus the low-target PBBS problem does not require one packet state capable
of serially realizing every parity/singleton pattern.  It is sufficient to
construct one coordinate-covariant packet template per target and then
plant all of them in parallel.

This quantifier swap is especially relevant after the native odd-step and
mixed-singleton no-go theorems.  A target with `t` maximal coordinate runs
may use `t-1` target-specific source seams; because `t<=|S|<=d`, such a
packet still has polynomial size.  Theorem 3.1 then removes the
cross-target packing issue.

## 5. Exact remaining qualifications

The theorem is only a resource-packing statement.  Three further rows must
be proved before it yields an OR word.

1. **Literal packet construction.**  A clean-C6/common-history source
   splice must actually concatenate the run fragments without introducing
   a label outside `S`, while preserving its full protected halo.
2. **Protected-factor extension.**  A degree-two bank of size `2^{o(n)}`
   must extend to the required owner/`q1` factor with the upper and
   residence decorations retained.  Fixed-bank extension alone is not
   enough; one needs the corresponding uniformly bounded-exposure
   extension theorem.
3. **Global chronology.**  The residual factor components must be joined
   and opened without deleting the planted low cells or their upper
   witnesses.

The new theorem closes only the alleged scarcity of disjoint physical
resources for a target-specific low packet atlas.  It does not claim a
PBBS seam, a completed factor, `B(k)+O(1)`, or exact equality.

