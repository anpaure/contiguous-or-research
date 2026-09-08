# Audit: coprime-voltage localization and the fixed-`z` completed-ticket subatlas

**Date:** 2026-08-02  
**Lane:** A, voltage-local repair and bounded-load fixed-`z` tickets  
**Verdict:** the central voltage-localization theorem is exact on the
co-oriented one-cycle face, with no hidden fixed-`z` phase mismatch.  An
explicit two-bank collar gives `Theta(k^7)` locally completed central
tickets with `O(d)` support and `O(k^6)` load on every nonprivate local
resource.  Exterior socket acceptance, zero total sidecar displacement,
deep upper/source/compiler return, and a child-native voltage seed remain
separate gates.

## 1. Exact signed fragment ledger

Let an oriented quotient cycle be cut into directed retained fragments
`P_j`.  Let `epsilon_j` be `+1` if the new chronology uses `P_j` in its old
orientation and `-1` if it reverses it.  For old seams `E` and new seams
`N`,

\[
 V(F')-V(F)
 =\sum_j(\epsilon_j-1)V(P_j)
   +\sum_{e\in N}\delta(e)-\sum_{e\in E}\delta(e).     \tag{1.1}
\]

Thus zero seam displacement preserves voltage under the proof-safe
hypotheses that every retained fragment is co-oriented and the output is
one quotient cycle.  Reversed fragments may cancel only after the signed
first term in (1.1) is checked.  If the output splits, there is no single
component voltage to iterate.

## 2. Fixed-`z` phase audit

In the required step-two orientation, the retained fragment `P_i` runs
from `x_i` to `y_(i+1)`.  The old and new seams are therefore

\[
                   y_i\longrightarrow x_i,
        \qquad     y_i\longrightarrow x_{i+1}.         \tag{2.1}
\]

In the phasewise fixed-`z` representatives both seam families have zero
intrinsic shift.  After a consistent endpoint gauge change `g`, their sums
are

\[
 \sum_i(g(x_i)-g(y_i)),\qquad
 \sum_i(g(x_{i+1})-g(y_i)).                            \tag{2.2}
\]

They agree because cyclic reindexing permutes the seven `x` endpoints.
Hence the central fixed-`z`, `h=0` heptagon has exact zero directed seam
displacement.  The common label `z` closes the cap rotor; it is not the
reason for (2.2).

There is no hidden phase mismatch in the retained rays: the old and new
states use each ray in the same direction, so its signed contribution
cancels.  This statement does not cover added cap/history/aperture/join
seams.  Their contributions must be added to the complete-ticket ledger,
and the required total is zero.

Consequently one coprime pump suffices within one fixed cyclic modulus.
After a Pascal modulus change, a fresh or transported child-native unit
seed is still required.

## 3. Explicit fixed-`z` local atlas

For one rooted task `(X,a)`, choose disjoint ordered deletion banks
`D^x,D^y` in `X-{a}` and marker banks `M^x,M^y` outside `X`, all of length
`d`.  Restrict the two internal and five external heptagon roles to avoid
the appropriate banks.  The exact number of surviving central packets is

\[
 N_d=(r-1-2d)_2(k-r-2d)_4(k-r-2d-4).                  \tag{3.1}
\]

For central endpoint `E` of type `epsilon`, attach the monotone ray

\[
 E_j=(E-D^\epsilon_{[j]})\cup M^\epsilon_{[j]},
                     \qquad 0\le j\le d.              \tag{3.2}
\]

For either terminal state, the heptagon plus fourteen rays is a simple
2-bounded incidence path bank with

\[
 |V_O|=14+14d,qquad |V_F|=7+14d,qquad |E|=14+28d.    \tag{3.3}
\]

The full old/new collision ledger has `21+28d` incidence edges and packet
facets of degree three; it is not itself the protected terminal bank.

Traversing each `y` ray inward and each `x` ray outward exposes past
positive/negative banks `(D^y,M^y)` and future banks `(D^x,M^x)`.  Their
disjointness proves every triangular depth-`d` cross-collar inequality for
both old seams and new seams.  No short run is completed wholly inside one
ray.  The far endpoints export partial history relations; their exterior
halves are not automatically accepted.

## 4. Exact load and privacy boundary

The private closure must contain

\[
 \mathcal P_{X,a}=\{X,X-\{a\},(X,X-\{a\})\}
 \cup\{\text{all owner/facet/incidence/cap/history occurrences
                      on the full }X\text{-ray}\}.      \tag{4.1}
\]

Without (4.1), the fixed incidence `(X,X-{a})` has load `N_d`, giving a
literal `Theta(k^7)` counterexample.  History resources must remain fully
occurrence-labelled; bare bank-label pairs also have excessive load.

Central packet resources obey the original direct `K_0k^6` bound.  Every
nonprivate ray/collar extension decodes to at most two central endpoints by
its marker prefix.  Hence every nonprivate local resource has load at most
`2K_0k^6`.

For `H` tasks, pairwise compatibility of private labels is not enough.
Prefilter atlas `i` against every foreign private closure.  If
\(p_d=\max_i|\mathcal P_i|=O(d)\) and `S_d=O(d)` is the nonprivate ticket
support, a sufficient greedy inequality is

\[
             N_d>2K_0(H-1)(p_d+S_d)k^6.               \tag{4.2}
\]

Thus fixed `H` and `d=o(k)` give a resource-disjoint local transversal.

The use of two disjoint banks is a sufficient construction, not a necessity
theorem.  A shared bank in the same effective order may violate the guard;
antitone reuse has `s+t=d+1` and passes the triangular inequality.  No
simplicity/decoder theorem for that one-bank variant is claimed.

## 5. Literal cap-provider scope

The protected provider theorem applies here only after specializing to the
Middle-Levels host `k=2r-1`.  Backup count `q` is literal request
multiplicity.  For one selected terminal bank plus exterior sidecars with
complete counts `(v_O,v_F,L)`, the sufficient conditions are

\[
 {r+1-v_O-2q\choose2}>v_F+q,
             \qquad L+2q\le r-2.                      \tag{5.1}
\]

For `H` tickets, (5.1) must be applied once to their selected union, with
aggregate `V_O,V_F,L,q_tot`; separate per-ticket completions do not give a
common factor.  The provider theorem gives a static owner/facet two-factor
and named cap support.  It gives neither one-cycle topology nor history
acceptance, and its literal physical edge budget cannot be multiplied by a
full quotient orbit without a new equivariant extension theorem.

## 6. Sharp remaining gate

The bounded-load fixed-`z` central/collar row is closed.  A fully completed
ticket still requires a continuation of the fourteen far sockets such that

1. the seven old cuts lie on one co-oriented quotient cycle in step-one
   order;
2. the step-two rethread is one quotient cycle;
3. all exterior positive and negative history relations accept;
4. the aggregate directed displacement of all added sidecar seams is zero
   (or is explicitly balanced in the complete ledger); and
5. deep upper, source/compiler, and aperture rows return, and a child-native
   unit-voltage seed is supplied.

The raw `Theta(k^7)` central count alone does not prove that correlated
continuation theorem.

## 7. Frozen provenance

Audited sources:

```text
51c1328778474ce04a646e3e869454b2b8877ece67c7749ea5e82ea700344582
  MATH_THEOREM_K17_ORIENTATION_FREE_SHORT_RUN_CLAUSES_AND_VOLTAGE_LOCALIZATION_20260802.md

1a436267a1a71d9a49bee6eb3fa83d62ea1f6529a50d27029c3e4716f491bdfd
  MATH_THEOREM_A_FIXED_Z_TWO_BANK_DECODABLE_HISTORY_COLLAR_AND_BOUNDED_LOAD_SUBATLAS_20260802.md
```

Independent audits also used:

* `MATH_AUDIT_A_ZERO_HOLONOMY_FRAGMENT_ORIENTATION_AND_SPLIT_COUNTEREXAMPLES_20260802.md`;
* `MATH_AUDIT_A_FIXED_Z_ZERO_DISPLACEMENT_AND_COMPLETED_TICKET_LOAD_GATE_20260802.md`;
* `MATH_AUDIT_A_FIXED_Z_TWO_BANK_COLLAR_COUNT_HISTORY_LOAD_AND_SCOPE_20260802.md`; and
* `MATH_AUDIT_A_FIXED_Z_TWO_BANK_COLLAR_PRIVACY_AND_SCOPE_20260802.md`.

No finite search, SAT result, or independent-marginal overlap assumption is
used.
