# The two-coordinate rotation is not an MSW factor automorphism

**Date:** 2026-08-07  
**Method:** endpoint-set rigidity; no computation or search  
**Status:** unconditional.

Let `rho` rotate the last two coordinates of a balanced word to the front.
For the q2 relay prefixes,

\[
                         \rho(11101101\,10)=10\,11101101. \tag{1.1}
\]

This word identity does not conjugate a local switch inside the canonical
MSW selected-incidence factor.

### Theorem

For every `m>=3`, `rho` is not an automorphism of the canonical MSW
incidence-path factor at semilength `m`.

#### Proof

The factor is the disjoint union of the canonical paths `P(x)`, `x in D_m`.
Its degree-one rank-`m` vertices are exactly

\[
                         D_m\cup\overline{D_m}. \tag{1.2}

Take `x=1^m0^m`.  It is Dyck.  But

\[
                         \rho(x)=00\,1^m0^{m-2}       \tag{1.3}

starts with a down-step and is not Dyck.  Its complement is

\[
                         11\,0^m1^{m-2}.              \tag{1.4}

After the two initial up-steps, the block of `m` down-steps reaches height
`2-m<0`; hence (1.4) is not Dyck when `m>=3`.  Therefore `rho(x)` belongs to
neither shore of (1.2).

Any automorphism of the selected path factor preserves vertex degrees and
must map its endpoint set to itself.  Equation (1.3) contradicts this.
\(\square\)

### Corollary

A global application of `rho` sends the canonical factor to an isomorphic
but different factor.  It cannot import the `B8 10` relay as a local repair
of `10 B8` while retaining the original factor, protected pivot, and MNW
interfaces.  The minimal valid replacement is a literal annulus joining
the natural `01` context to the desired `10` context, with the boundary,
turn-provider, topology, and protection conditions stated in the
one-prefix prepared-prism lemma.
