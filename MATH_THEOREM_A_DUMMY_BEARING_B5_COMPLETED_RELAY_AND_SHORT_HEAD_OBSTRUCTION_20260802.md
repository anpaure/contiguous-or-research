# Dummy-bearing Boolean relays, the completed-slot criterion, and the
# short--head obstruction

**Date:** 2026-08-02  
**Lane:** A, bottom-token common-base and private socket tickets  
**Status:** exact local theorem and fixed-suffix impossibility theorem.  The
positive relay below preserves the completed bottom-table target deck and
the stated moving co-middle deck.  It does **not** preserve the typed
real-interval head/upper deck, and it does not by itself furnish a literal
common-state socket.  No K17 chronology, residence, upper-shadow, topology,
source, compiler, or word conclusion is claimed.

## 0. Verdict

There are two different resource ledgers, and they must not be conflated.

1. In the **completed hard-slot ledger**, every hard slot contributes its
   fixed suffix `(M_v,U_v)` whether it is long or short.  A real bottom on
   the slot contributes one additional moving resource
   
   \[
                      \chi(B;v)=B\cup(U_v-M_v).
   \]
   
   In this ledger a support-minimal dummy-bearing `C4` exists.  If two
   suffixes have the same added cap point, the `C4` moves the dummy, hence
   exchanges one short slot, while preserving the outer target partition
   and the complete `chi` deck.  Puncturing the hub `C6` or hub `C8` gives
   respectively a three-choice or four-choice version.

2. In the **typed real-interval ledger**, only a real-occupied slot supplies
   its interval head `M_v` and interval upper `U_v`.  On a coefficient-one
   table with distinct fixed suffixes,
   
   \[
          \operatorname{mult}_{\rm head}(M_v)=1-s_v,
          \qquad
          \operatorname{mult}_{\rm upper}(U_v)=1-s_v.       \tag{0.1}
   \]
   
   Therefore every move preserving either complete typed palette fixes the
   short vector pointwise.  No dummy-bearing `B5` circuit, and no larger
   collection of fixed-suffix `C6/C8/C10` companions, can change a basis of
   `M_short` while preserving those rows.

Thus the present Boolean atlas gives an exact short-basis actuator only on
the completed-slot/co-middle projection.  It does not yet realize the
full private common-state matroid `M_sock`.  The first possible full escape
must move an entire suffix/guard packet between physical roles, or weaken the
typed head/upper requirement.  Such a move is outside the frozen
bottom-token matroid and must be selected in a joint chain/slot master.

## 1. The exact completed-signature criterion

Let `V` be a fixed hard-slot set.  Slot `v` carries a fixed suffix

\[
                       M_v\subsetneq U_v.                    \tag{1.1}
\]

Let `P` be a matching of a fixed real-bottom palette `Bcal` together with
dummy tokens into `V`.  A slot is short precisely when its matching edge
has a dummy endpoint.  Assume the complete local resource signature has
the following form.

* Every slot `v` contributes a fixed vector `tau(v)` in both long and short
  mode.  This vector may contain its named `M_v,U_v`, fixed cap, owner, root,
  and any other status-independent resource.
* Every real edge `Bv` contributes the real-bottom label `B` and a moving
  named-resource incidence vector `sigma(B,v)` in the free abelian group on
  all declared moving rows.  A dummy edge contributes neither.

This is exactly the decomposition supplied by the bottom-token theorem
when the only extra moving interval resource is `chi`.

### Theorem 1.1 (completed-signature equivalence)

Let `P_0,P_1` use the same slot set, the same real-bottom palette and the
same number of dummies.  Then their completed resource vectors agree if and
only if

\[
 \boxed{
   \sum_{Bv\in P_0,\ B\text{ real}}\sigma(B,v)
   =
   \sum_{Bv\in P_1,\ B\text{ real}}\sigma(B,v).}
                                                               \tag{1.2}
\]

In particular, for the Boolean bottom relay one may take

\[
                  \sigma(B,v)={\bf e}_{\chi(B;v)},             \tag{1.3}
\]

where `e_X` is the formal unit vector of named co-middle `X`; in that case
(1.2) is exactly equality of the two `chi` multisets.

#### Proof

Both modes contain the same fixed sum `sum_v tau(v)`.  They also use every
real bottom exactly once, so the real-bottom label sum agrees.  After those
common rows are cancelled, the only remaining row is the incidence sum in
(1.2).  This proves necessity and sufficiency.  Formula (1.3) is the exact
co-middle decomposition of a Boolean diamond.  \(\square\)

The theorem does not apply to a transition-dependent flag, address, or
history label unless that label has actually been included in `tau` or
`sigma` with the displayed factorization.  In particular, deck equality of
`chi` does not imply common-state compatibility.

## 2. The support-minimal dummy `C4`

Fix a rank-`q` bottom `B` and distinct coordinates `x,y,z` outside `B`.
Take two distinct hard slots

\[
\begin{array}{c|cc}
       &M&U\\ \hline
 v_0&B+x&B+x+z\\
 v_1&B+y&B+y+z.
\end{array}                                                   \tag{2.1}
\]

Let `u` be one dummy.  The two local matchings are

\[
       P_0=\{uv_0,Bv_1\},\qquad
       P_1=\{Bv_0,uv_1\}.                                    \tag{2.2}
\]

### Theorem 2.1 (minimal completed-slot short exchange)

The symmetric difference in (2.2) is one alternating `C4`.  It changes the
short set from `{v_0}` to `{v_1}`, preserves the complete outer target
partition, and preserves the moving co-middle literally because

\[
                  \chi(B;v_0)=B+z=\chi(B;v_1).                \tag{2.3}
\]

More generally, a one-real-bottom/two-slot dummy `C4` preserves a declared
moving signature `sigma` if and only if

\[
                         \sigma(B,v_0)=\sigma(B,v_1).           \tag{2.4}
\]

For the named `chi` ledger, (2.4) is equivalent to equality of the two
added cap points `U_v-M_v`.

No smaller matching support can change a short slot.  Thus (2.2) is
support-minimal on the completed ledger.

#### Proof

Both real edges are legal by (2.1).  Each mode matches the same real bottom,
dummy and two slots exactly once.  The materialization theorem therefore
gives the same named targets `B,M_{v_0},U_{v_0},M_{v_1},U_{v_1}` exactly
once.  Equation (2.3) and Theorem 1.1 give completed-signature equality.
Conversely, after the fixed and bottom rows are cancelled, a `C4` has one
moving signature on each side, so equality is exactly (2.4).  A nonidentity
matching exchange needs at least two left and two right vertices.  \(\square\)

This `C4` is not a counterexample to the absence of a complete two-diamond
trade in the `B5` interval atlas.  Its real interval has head/upper
`(M_{v_1},U_{v_1})` in `P_0` and `(M_{v_0},U_{v_0})` in `P_1`.  Those typed
real-interval palettes are different.  They agree only after the short
row's fixed suffix is included in the completed table ledger.

## 3. Punctured hub tickets

The minimal `C4` extends to an exact finite menu directly from the
authenticated hub atlas.  Let `r>=3`, choose a `(q-1)`-set `C`, a hub `h`,
and distinct rim coordinates `a_0,...,a_{r-1}` outside `C+h`.  Put, with
indices modulo `r`,

\[
\begin{aligned}
 B_i&=C+a_i &&(1\le i\le r-1),\\
 M_i&=C+a_i+a_{i+1},\\
 U_i&=C+h+a_i+a_{i+1}.                              \tag{3.1}
\end{aligned}
\]

Use hard slots `v_i` with suffix `(M_i,U_i)` and one dummy `u`.  For
`0<=j<=r-1`, define

\[
 P_j=\{uv_j\}
   \mathbin{\dot\cup}\{B_i v_{i-1}:1\le i\le j\}
   \mathbin{\dot\cup}\{B_i v_i:j<i\le r-1\}.       \tag{3.2}
\]

### Theorem 3.1 (punctured-hub outer partition block)

Every `P_j` is a perfect matching of the displayed local shores and has
short set `{v_j}`.  All `r` modes have the same completed target and
co-middle decks:

\[
       \{\!\{\chi(B_i;P_j(B_i)):1\le i\le r-1\}\!\}
       =\{\!\{C+h+a_i:1\le i\le r-1\}\!\}.          \tag{3.3}
\]

Adjacent modes differ by the dummy `C4`

\[
          uv_{j-1},\ B_jv_j
          \quad\longleftrightarrow\quad
          B_jv_{j-1},\ uv_j,                        \tag{3.4}
\]

and the two extreme modes differ on one alternating `C_(2r)` containing
the dummy.  For `r=3` and `r=4`, this is respectively a punctured hub `C6`
and punctured hub `C8`; they fit inside `B5` (with one unused coordinate in
the `C6` case).

Consequently, on the completed outer/co-middle projection only, a completely
private planted copy presents a rank-one partition-matroid block with bases
`{v_0},...,{v_{r-1}}`.  Pairwise complete-footprint-disjoint copies give a
direct sum of such blocks, hence a transversal matroid on that projection.
This is not yet a socket-ticket matroid because common-state legality has
not been supplied.

#### Proof

Bottom `B_i` is contained in both `M_{i-1}` and `M_i`, so every edge in
(3.2) is legal.  The path incidence forces one matching for each omitted
slot `v_j`.  Both possible placements of `B_i` have the common added cap
point `h`, hence

\[
              \chi(B_i;v_{i-1})=C+h+a_i=\chi(B_i;v_i),
\]

which proves (3.3).  Formula (3.4) is immediate, and composing the adjacent
switches gives the extreme alternating cycle.  Singleton choices in a
disjoint block are the bases of \(U_{1,r}\); direct sums of partition
matroids are transversal.  \(\square\)

The word **private** is load-bearing.  Every mode forces all other slots in
its block long.  Thus overlapping punctured-hub blocks do not automatically
give an arbitrary transversal ticket graph.  The conclusion above applies
to blocks whose complete footprints, not merely their selected short slots,
are disjoint.

### Proposition 3.2 (the saturated `B5 C10` does not puncture)

Use the saturated relay notation

\[
 B_i=C+a_i,\quad M_i=C+a_i+a_{i+2},\quad
 U_i=C+a_i+a_{i+1}+a_{i+2}                         \tag{3.5}
\]

on indices modulo five.  Its two closed modes put `B_i` respectively on
`v_i` and `v_(i-2)`.  If one deletes `B_j` and replaces it by a dummy, the
two missing co-middle labels are

\[
       \chi(B_j;v_j)=C+a_j+a_{j+1},\qquad
       \chi(B_j;v_{j-2})=C+a_{j-1}+a_j.             \tag{3.6}
\]

They are distinct.  Therefore puncturing the authenticated saturated
`C10` does not preserve the completed `chi` deck and does not furnish a
unary ticket.  This contrasts with the hub `C6/C8`, whose added cap point is
constant around the whole rim.

#### Proof

Formula (3.6) follows directly from `U_i-M_i={a_(i+1)}`.  The five rim
coordinates are distinct, so its two values differ.  The original closed
`C10` co-middle decks were equal; deleting unequal entries from them leaves
unequal punctured decks.  \(\square\)

This proposition concerns the literal puncture of the saturated `C10`.
It does not classify every possible five-slot dummy rail with a different
suffix geometry.

## 4. The full typed-palette obstruction

Let the fixed suffix heads `M_v` be pairwise distinct in the complete
occurrence-labelled typed-head row, as they are in a coefficient-one target
partition.  For a bottom matching `P`, let `s_v(P)` be the short indicator
and let `H_P` be the
typed real-interval head multiplicity vector.  Since a real-occupied slot
contributes its fixed head once and a dummy-occupied slot contributes no
real interval,

\[
                         H_P(M_v)=1-s_v(P).                     \tag{4.1}
\]

The same formula holds for the typed interval-upper vector when the `U_v`
are pairwise distinct.

### Theorem 4.1 (short--head free-cokernel obstruction)

On a fixed coefficient-one suffix table, any move preserving the complete
typed real-interval head palette fixes the short set pointwise.  The same is
true if one preserves the complete typed interval-upper palette.  Hence no
dummy-bearing actuator which changes a basis of `M_short` can preserve all
four interval palettes on that fixed table.

This remains true after adjoining any number of dummy-free `C6`, `C8`, or
`C10` circuits, after allowing overlapping circuits, and after increasing
the support beyond `B5`.

#### Proof

Subtract (4.1) for the two modes.  Typed-head equality gives

\[
                         0=\Delta H(M_v)=-\Delta s_v
                         \qquad(v\in V),                         \tag{4.2}
\]

so the short vector is fixed.  The upper proof is identical.  A dummy-free
circuit has `Delta s=0`, so adding any sum of such circuits cannot change
(4.2).  The argument uses no support-size assumption.  \(\square\)

Equation (4.2) is a free, coordinatewise obstruction, not a parity or
torsion obstruction.  In Smith-form language, every fixed suffix occurrence
has the conserved row

\[
                       H(M_v)+s_v=1,                           \tag{4.3}
\]

and similarly `U(U_v)+s_v=1`.  Thus no aperture count or core-flux circuit
inside the frozen suffix table can remove it.  The `B5 C8` aperture is an
omitted interval of a resource fibre; it is not a dummy-matched hard slot.

### Corollary 4.2 (exact B5 scope)

The `C4` of Section 2 and punctured hub modules of Section 3 are exact only
for the completed-slot/co-middle projection.  Calling them complete
four-palette Boolean actuators would be false.  Conversely, a claimed B5
companion which leaves every suffix occurrence fixed cannot compensate the
head/upper boundary: Theorem 4.1 rules it out before any B5 catalogue is
enumerated.

## 5. The first common-state obstruction

Even on the weaker completed ledger, the minimal `C4` does not automatically
give a literal common-state socket.  Let its two chain roles be

\[
 A=(B\subset B+x\subset B+x+z),\qquad
 S=(B+y\subset B+y+z),                                \tag{5.1}
\]

where `x,y,z` are distinct outside `B`.  These are respectively the long
state of one endpoint and the short state of the other.

For clarity, the canonical three-cell flags used below are the following.
Writing `1,2,3` for the cell positions, a long chain
`B subset M subset U` uses one of

\[
 (1,12,123),\ (2,12,123),\ (2,23,123),\ (3,23,123),       \tag{5.2}
\]

where the entries are the supporting intervals of `B,M,U`.  A short chain
`M subset U` uses either `(12,123)` or `(23,123)`.  Each named target is the
union of the cells in its displayed interval, and every cell is nonempty.

### Proposition 5.1 (direct-adjacency no-go)

No canonical three-cell source realizes `A` immediately followed by `S`.
The reverse direction is impossible by reflection.

#### Proof

The consecutive three-cell windows share two cells.

* If the short `P1` target `B+y` uses its `12` state, the two shared cells
  have union exactly `B+y`.  But both shared cells lie in the preceding
  long upper `B+x+z`, which omits `y`.
* If the short target uses its `23` state, the first shared cell is outside
  its `P1` interval and must contain `z`.  This cell is the middle cell of
  the preceding long window.  In all four canonical long flags that middle
  cell is bounded above by either `B` or `B+x`, so it cannot contain `z`.

Both short flags are excluded.  Reflecting the five source positions proves
the reverse statement.  \(\square\)

### Corollary 5.2 (minimum linear collar size)

Suppose both candidate short roles of a two-mode ticket must be internal in
one simple linear role order and each needs a predecessor and successor long
role from that order.  Then a direct-adjacency-forbidden ticket needs at
least five chain roles: the two candidates, one separating role, and one
outer guard on each side.  A possible order has the form

\[
                         g_0,e_0,g_1,e_1,g_2.                  \tag{5.3}
\]

This is a lower bound, not an existence theorem.  The authenticated B5
`C6/C8/C10` atlas supplies no literal five-role common-state collar or
mode-transparent exterior ports.  Consequently Sections 2--3 do not yet
construct the physical `M_sock` required by the common-base theorem.

## 6. The first admissible escape type

Theorem 4.1 shows that a larger fixed-suffix circuit is not the answer.  A
full-signature short exchange must leave the frozen bottom-only face.  The
support-minimal algebraic escape is a **complete role transposition**.

Let `A` be one complete short-role packet and `L` one complete long-role
packet, including their suffix, owner/root attachment, typed head/upper,
state, history, cap and guard labels.  On two physical sites `p,q`, compare

\[
\begin{array}{c|cc}
      &p&q\\ \hline
 \text{mode 0}&A&L\\
 \text{mode 1}&L&A.
\end{array}                                                    \tag{6.1}
\]

As a labelled multiset, every resource is identical and the physical short
site changes from `p` to `q`.  Thus (6.1) is the smallest formal companion
which cancels both `+M_p-M_q` and `+U_p-U_q`: it transports the entire packet
instead of trying to repair its projections separately.

However, (6.1) is not an edge of the fixed cotransversal matroid
`M_short=(M/F)^*`, because that matroid was defined after the suffix packet
at each physical site was frozen.  A literal realization must be selected
in a joint chain/slot/owner master, and Proposition 5.1 shows that an internal
two-ended common-state version needs at least the five-role collar (5.3).

Accordingly the exact next positive target is:

> construct a five-role (or larger) moving-suffix Boolean collar whose two
> modes realize (6.1), have identical exterior port signatures, and replay
> every common-state/cap/guard row; then prove a private or matroidal packing
> theorem for those collars.

Without that moving-packet step, the present B5 circuits remain internal
routers over a fixed short basis or completed-ledger status relays.  They do
not realize the full socket matroid face.

## 7. Scope ledger

Proved:

* the exact completed-signature criterion;
* the support-minimal dummy `C4` and all-dimensional punctured-hub menu;
* an explicit partition-matroid subface for disjoint completed modules;
* the dimension-uniform fixed-suffix short--head/upper obstruction;
* the canonical direct-adjacency common-state no-go and five-role lower
  bound; and
* the exact moving-role interface required to escape.

Not proved:

* a literal five-role moving-suffix collar;
* a rank-1748 private ticket planting;
* matroidality of the actual shared-state socket system;
* compatibility with residence, deep upper shadows, topology, source, or a
  compiler; or
* any new K17 word or all-dimensional equality theorem.
