# Audit: fixed-`z` zero displacement and the remaining completed-ticket load gate

**Date:** 2026-08-02  
**Lane:** A, retained-fragment voltage and fixed-`z` ticket abundance  
**Status:** the central voltage/topology calculation passes with exact
orientation.  The completed-ticket and same-parity transport conclusions
remain conditional.  No finite search is used.

## 0. Verdict

The voltage-localization identity is correct when the output uses every
retained fragment in its old orientation and forms one quotient cycle.  In
the odd step-two orientation of the fixed-`z` heptagon, the old seam in row
`i` is literally

\[
                         y_i\longrightarrow x_i,
\]

and the new seam is

\[
                         y_i\longrightarrow x_{i+1}.
\]

Their total voltage difference is zero in every consistent endpoint gauge.
There is no hidden sign or index shift in the central `C14`.

Three qualifications are load-bearing.

1. Zero displacement is proved for the **central** `C14`; every history,
   aperture, backup, opening, or joining seam in a completed ticket must be
   included in the displacement ledger.
2. A local `h=0` label is not topology.  Fragment reversal or a multi-cycle
   output invalidates the scalar one-cycle conclusion.
3. A coprime seed is preserved only inside one fixed cyclic cover.  A Pascal
   dimension step changes the modulus and requires a child-native unit
   voltage certificate.

Accordingly the twisted high-load atlas can be confined to one seed per
child modulus, but the fixed-`z` completed-ticket abundance theorem is still
open.

## 1. Exact retained-fragment ledger

Let a directed quotient cycle `F` be cut into directed retained fragments
`P_0,...,P_(t-1)`.  Write `p_i=delta(P_i)`.  Let `E` and `E'` be the old and
new directed seam multisets.  If the output traverses `P_i` with sign
`epsilon_i in {+1,-1}`, then

\[
 V(F')-V(F)=
   \sum_i(\epsilon_i-1)p_i
   +\sum_{e\in E'}\delta(e)-\sum_{e\in E}\delta(e).    \tag{1.1}
\]

This identity follows by writing the two cycle voltages and subtracting.
It gives the exact boundary of localization:

* when every `epsilon_i=+1` and the seam displacement is zero, voltage is
  preserved;
* reversing a fragment contributes `-2p_i`;
* if the output has several cycles, each cycle needs its own fragment/seam
  sum and physical component count.

For a free `Z_n` cover, a quotient cycle of voltage `v` develops into
`gcd(n,v)` physical cycles.  Thus connectedness is equivalent to
`gcd(n,v)=1`; nonzero voltage is insufficient for composite `n`.

## 2. Independent fixed-`z` orientation check

The fixed-`z` circuit has old and new rows

\[
 e_i=\{x_i,y_i\},\qquad e_i'=\{x_{i+1},y_i\}.          \tag{2.1}
\]

The step-two topology theorem orients the retained fragments as

\[
                         P_i:x_i\leadsto y_{i+1}.       \tag{2.2}
\]

Hence after `P_(i-1)` the old cycle uses `e_i` as
`y_i -> x_i`.  After the switch it uses `e_i'` as
`y_i -> x_(i+1)`, and then enters `P_(i+1)`.  Equivalently, after `P_i` the
new path index advances `i -> i+2`.  This is exactly the orientation needed
by the odd step-two theorem.

Choose any consistent quotient section and let `g(w)` be the endpoint
potential.  Then

\[
\begin{aligned}
 \sum_i\delta(y_i,x_i)
   &=\sum_i\bigl(g(x_i)-g(y_i)\bigr),\\
 \sum_i\delta(y_i,x_{i+1})
   &=\sum_i\bigl(g(x_{i+1})-g(y_i)\bigr).
\end{aligned}                                           \tag{2.3}
\]

The two sums agree because `i -> i+1` permutes the seven moving endpoints.
Thus

\[
                         \sigma_{C14}=0.                \tag{2.4}
\]

The calculation is gauge invariant.  In the natural phasewise
representatives all old and new seam voltages are individually zero.  The
common label `z` proves cap-multiset transport and separates moving from
retained owners; it is not needed for the telescoping identity (2.4).

The global reversal also has zero displacement: it replaces the two sums by
their negatives.  A mixture of fragment orientations is different and is
governed by (1.1), not by (2.4).

## 3. Exact topology qualification

If the old quotient factor contains the seven seams in the orientation
(2.2), the new seams advance fragment indices by two.  Since seven is odd,
this is one quotient cycle.  Therefore the fixed-`z` packet is a qualified
zero-displacement rethread on precisely this host face.

This statement does not cover the seven-component absorber version.  When
old seams lie on different cycles, there is no single old voltage to which
the scalar localization identity applies.  After merging, the output
voltage must be computed from all oriented fragment voltages and new seams.

It also does not automatically compose for an arbitrary disjoint packet
set.  A first rethread can change the cyclic order seen by the second packet.
For serial localization, every prefix must again satisfy the one-cycle,
same-orientation step-two predicate.  Alternatively, the whole simultaneous
symmetric difference must be replayed once in the full retained-fragment
ledger.

## 4. One seed suffices, with two exact corrections

Suppose a one-cycle quotient host over `Z_n` has voltage `v` with
`gcd(n,v)=1`.  A serial sequence of qualified zero-displacement completed
tickets preserves `v` at every prefix, hence preserves a connected physical
lift.

The phrase “one exceptional voltage ticket” is proof-safe only when that
exceptional construction is certified to leave the **total output host** at
a unit voltage.  A packet having nonzero or coprime local seam displacement
does not by itself imply this, because it acts by

\[
                         v\longmapsto v+\sigma.         \tag{4.1}
\]

The second correction concerns induction.  Passing from `Z_n` to
`Z_(n+2)` does not transport a generator functorially.  For odd `n`, every
homomorphism `Z_n -> Z_(n+2)` is trivial because
`gcd(n,n+2)=1`.  Even the same integer can change status: `3` is a unit
modulo `7` and not modulo `9`.  Each child therefore needs a child-native
unit-voltage seed (preferably `+1` or `-1`) before the zero-displacement
localization argument begins.

## 5. Total displacement of a completed ticket

A completed fixed-`z` ticket can contain the central switch, history/reset
collars, cap providers or active returns, a Pascal aperture discharge, and
topology/opening seams.  Its exact voltage coordinate is

\[
 \sigma_{\rm tot}=sigma_{C14}
   +\sigma_{\rm hist}+\sigma_{\rm cap}
   +\sigma_{\rm aperture}+\sigma_{\rm join}.           \tag{5.1}
\]

Equation (2.4) removes only the first term.  Cap support, cap-multiset
equality, and history acceptance do not imply that the other four terms sum
to zero.  Therefore the recursive packet state must retain `sigma_tot`, or
the completed sidecars must be constructed as inverse/zero-current pairs.

The protected duplicate-provider theorem is also literal and size-limited.
It applies to a selected physical bank only under both its clique-availability
inequality and `L+2q<=m-2`.  It cannot be applied verbatim to the full
`Z_k` development of a quotient `C14`, whose central incidence bank already
has `14k` edges.  The central fixed-`z` packet is cap-multiset exact, so no
central backups are needed; any provider use concerns separately named
collar/aperture casualties and must respect the physical size scope.

## 6. Fixed-`z` bounded-load assessment

For a rooted central defect `(X,a)`, the prospective fixed-`z` atlas has

\[
 N_{k,r}=(r-1)(r-2)(k-r)_4(k-r-4)=\Theta(k^7)          \tag{6.1}
\]

in the central regime.  Its proved central load theorem gives

\[
       \deg(q)\le K_0k^6                                \tag{6.2}
\]

for every nonanchor moving owner, retained owner, facet, cap, or row token.
Unlike the fixed-root twisted geodesic atlas, its moving skeleton varies in
the seven role choices; there is no corresponding finite-skeleton
`Omega(k^7)` load obstruction.

There is a useful conditional history count.  Suppose that, on a fixed
retained-fragment table, acceptance of an admitted boundary socket deletes
only `A d` unary role values/equalities from the seven free-role atlas.  Each
bad equality fixes at least one role and therefore removes at most
`K_1k^6` central tickets.  Hence

\[
      N_{\rm accepted}\ge c k^7-AK_1d k^6
                         =\Omega(k^7)                  \tag{6.3}
\]

whenever `d=o(k)`.  The same union bound keeps nonanchor load `O(k^6)`.

Equation (6.3) is not a general history theorem.  A relation-labelled reset
entrance can reject an entire prescribed state fibre, and the raw central
count does not expose the old seams in one current factor.  The exact
remaining fixed-`z` supply theorem must simultaneously provide:

1. `Omega(k^7)` old/new occurrences in one admitted boundary-history fibre;
2. the one-cycle, co-oriented step-two retained-path predicate, stable under
   the intended serial or simultaneous packet composition;
3. zero **total** displacement (5.1), not merely (2.4);
4. `O(d)` literal history/collar support with `O(k^6)` occurrence load;
5. protected upper, source/compiler, and aperture return rows; and
6. a child-native unit-voltage seed once per new modulus.

Thus localization genuinely removes repeated twisted-voltage selection from
the repair atlas.  It does not by itself prove completed fixed-`z` ticket
abundance; the live gate is chronological/topological host exposure with a
zero-current sidecar.

## 7. Provenance and scope

This audit checks the retained-fragment statements against:

- `MATH_THEOREM_HEPTAGONAL_CAP_CIRCULATION_AND_PROSPECTIVE_ABUNDANCE_20260802.md`;
- `MATH_THEOREM_A_HEPTAGONAL_CAP_BACKUP_AND_BIHISTORY_TICKET_INTERFACE_20260802.md`;
- `MATH_THEOREM_HEPTAGON_PROTECTED_HOST_AND_DUPLICATE_CAP_BACKUPS_20260802.md`; and
- `MATH_THEOREM_K17_ORIENTATION_FREE_SHORT_RUN_CLAUSES_AND_VOLTAGE_LOCALIZATION_20260802.md`.

It makes no physical ticket, Pascal child, deeper-upper, source/compiler, or
universal-word existence claim.
