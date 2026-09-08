# Audit: the fixed-neighbour coatom fibre is exact, but a full inverse ray twin cancels the physical q1 root

Date: 2026-08-01  
Audited targets:
`MATH_THEOREM_L_LABELLED_HIGH_SEPARATOR_RIGIDITY_AND_PULL_CLOCK_RAY_GATE_20260801.md`
and
`MATH_THEOREM_L_TRANSITION_COATOM_RIGIDITY_AND_PAIRED_UPPER_CURRENT_20260801.md`.  
Scope: independent symbolic audit of Sections 4--6.  No finite search or
compiler-existence claim is used.
Status: `PASS_AFTER_STUTTER_LOWER_RAY_AND_CAPACITY_ONE_CORRECTIONS` for the
patched theorem note.

## 0. Verdict

The fixed-neighbour fibre and its exact `d`-cell ray are correct.  Two scope
corrections and one substantive correction are required.

1. A nontrivial singleton-terminal fibre necessarily sits on a repeated
   owner edge.  It is a literal equality/stutter separator, not a retiming
   of the coatom on a fixed nonloop Johnson edge.
2. The changed `d` source intervals are all proper subsets of the unchanged
   middle owner.  Hence they are lower/compiler cells.  The owner chronology
   and its complete upper interval deck are unchanged exactly.
3. Two inverse sites with identical contexts through length `d` cancel the
   physical length-`d` coatom occurrence too.  Their full interval-deck
   payload is zero.  Calling one site unmarked can leave a root only in an
   externally declared mark ledger; it is not a primitive root in the
   literal occurrence/provider deck.  To retain a physical q1 transfer, the
   longest cell must remain open, and the compensator's longest-cell change
   must be carried as explicit q1 collateral or absorbed by certified
   redundant providers.

Thus Sections 4--5 pass after terminology/scope repair.  Section 6 is a
valid zero-action compiler rectangle if the declared common cap state
exists, but not the claimed physical unit actuator.

## 1. Exact fixed-neighbour fibre

Let

\[
 Z\xrightarrow{B}X\xrightarrow{C}Y,
 \qquad B=X_0,\quad C=Y_0,
\]

be literal age transitions.  The recurrence is

\[
 X_{i+1}=Z_i\setminus B,\qquad
 Y_{i+1}=X_i\setminus C\quad(0\le i<d).
\]

If the newborn block is changed to `B'`, the incoming arc forces

\[
 X'_{i+1}=Z_i\setminus B'.
\]

The middle type is unchanged exactly when

\[
 |B'|=|B|,\qquad |B'\cap Z_i|=|B\cap Z_i|\qquad(0\le i<d).
\]

The outgoing age-one row is unchanged exactly when

\[
 B'\setminus C=B\setminus C,
\]

equivalently \(B'\mathbin{\triangle}B\subseteq C\).  That inclusion also makes every
later outgoing row equal, because deletion of `C` erases the complete
difference.  These are precisely (4.2)--(4.3) of the audited theorem.

Writing \(U=Z_0\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}Z_{d-1}\),
the middle owner is

\[
 T(X)=U\cup B.
\]

Therefore `T(X')=T(X)` exactly when

\[
                         B'\triangle B\subseteq U.
\]

This verifies the iff in (4.4), including changes of newborn labels which
are outside the preceding owner.

## 2. Singleton terminal fibre and the repeated-owner law

Restrict to changes inside

\[
                         S=Z_{d-1}\cap C
\]

and fix \(|B\cap S|\).  Put

\[
 B_K=(B\setminus S)\cup K,
 \qquad K\subseteq S,\qquad |K|=|B\cap S|.
\]

All cells `X_1,...,X_(d-1)` are fixed, while

\[
 X_d^K=R\mathbin{\dot\cup}(S\setminus K),
 \qquad
 R=(Z_{d-1}\setminus C)\setminus B.                 \tag{2.1}
\]

If `X_d` is a singleton and this fibre has more than one member, then
`R` is empty, \(|B\cap S|=|S|-1\), and every option is

\[
 K=S\setminus\{z\},\qquad X_d^K=\{z\}\qquad(z\in S). \tag{2.2}
\]

The owner `T` is fixed, so the length-`d` lower cell is the coatom

\[
                         Q_z=T\setminus\{z\}.         \tag{2.3}
\]

There is an additional forced fact.  Since `z in S subseteq C`, the next
newborn block refreshes the terminal element.  Every element of
`T-{z}` either is refreshed or survives.  Consequently

\[
                         T(Y)=T(X).                  \tag{2.4}
\]

So a nontrivial fibre (2.2) is possible only at a repeated rank-`r` owner.
This is the exact reason it does not contradict fixed-nonloop-edge coatom
rigidity.  It also identifies the resource honestly: the local primitive
is an equality/stutter owner whose two exterior flag states are returned.

The raw `K=1` calculation is correct.  For `d>=2`, replacing the permanent
label `p` by a member of `A_d` changes both the intersection with
`Z_0=p+A_1` and that with `Z_(d-1)=A_d`, so (4.2) excludes it.  At `d=1`
the two constraints coincide and the displayed exceptional fibre (4.8) is
literal.  When `A_1={q}`, its coatom changes from `T-{q}` to `T-{p}`.

## 3. Exact ray and unconditional upper transparency

Place `Z` at time `t-1`, `B_z` at `t`, and `C` at `t+1`.  For two options
`z,z' in S`, both labels last occurred at time `t-d`, are absent at times
`t-d+1,...,t-1`, and occur together in `C`.  The old newborn contains
`z'` but not `z`; the new newborn contains `z` but not `z'`.

An interval changes only if it contains time `t`, omits time `t+1`, and
omits time `t-d`.  These are exactly

\[
                         I_\ell=[t-\ell+1,t],
                         \qquad1\le\ell\le d.         \tag{3.1}
\]

Writing

\[
 H_\ell=(B\setminus S)\cup(S\setminus\{z,z'\})
          \cup\bigcup_{j=t-\ell+1}^{t-1}A_j,
\]

their literal values change as

\[
                         H_\ell+z'\longrightarrow H_\ell+z.
                                                               \tag{3.2}
\]

Neither exchanged label lies in `H_ell`, so the positive and negative
occurrence shores are disjoint, with multiplicity `d`.  At `ell=d`, (2.3)
gives the primitive coatom change.

Every interval in (3.1) is contained in the fixed owner `T`, and its
longest member is the proper subset `T-{z}` or `T-{z'}`.  Thus all changed
values have rank below `r`.  Moreover the complete owner sequence is fixed
by Section 1.  It follows that:

* every rank-above-`r` upper target and every owner-interval witness is
  unchanged literally;
* if `t-d` and `t+1` are internal source positions, the full prefix- and
  suffix-union boundary signatures are unchanged; and
* the only live physical debt is the nested lower/compiler ray (3.1).

This corrects the phrases "exported upper ray" and "not upper-transparent"
in the audited draft.

## 4. Exact guarded primitive actuator

The fibre already gives a concrete positive lemma without a twin.  Fix one
literal terminal cap state and a target-cell matching `M`.  Suppose:

1. all `d` cells `I_ell` in (3.1) are unused by `M`;
2. every other protected lower assignment is in a cell outside this ray;
3. `Q_z` has an external retained provider (so the retimed occurrence is a
   surplus), while `Q_(z')` is the target to be installed; and
4. the retimed source letter satisfies the same position envelope/pin state
   (which is automatic for the carrier replay, but must be declared for any
   additional source-position guard).

Retiming `z` to `z'` preserves `M` edge by edge, and its new length-`d` cell
can be assigned to `Q_(z')`.  The compiler rank rises by one.  Both exterior
age states, the owner/stutter, topology, residence of the fixed owner word,
and the complete upper deck are unchanged.  This is a literal primitive
augmenter under an exact **private-ray** hypothesis; no scalar free-cell
count implies that hypothesis.

The same physical ray may be used serially inside its coatom clique as long
as all intermediate targets retain their pre-existing providers and the ray
remains outside the carried matching until the terminal hole.  A path using
different sites is also serializable, but only occurrencewise: after site
`i` creates the intermediate target, reassign that target from site `i+1`
to site `i`, thereby freeing the complete private ray of site `i+1` before
its toggle.  In addition, the earlier toggles must leave site `i+1`'s full
fixed-neighbour fibre and pins literal; disjoint ray cells alone do not imply
the crossed transition from Theorem 1.1.  Thus the sites on one path must be
distinct/private and serially compatible (or the same site must regenerate
in its current state).  Strong connectivity of the target projection alone
does not supply these capacities; the global network must remain
occurrence-labelled or time-expanded.

## 5. Why the full inverse twin is zero-action

Suppose a second site performs the inverse retiming and has the identical
contexts `H_1,...,H_d`.  At every length, including `d`, its action is the
negative of (3.2).  Therefore

\[
 \Delta_{\rm intervals}=0,
 \qquad
 \Delta_{q1}=0                                             \tag{5.1}
\]

in the literal occurrence deck.  The `d` declared `K_(2,2)` compiler
rectangles are a sufficient common-state basis swap, but they do not alter
(5.1).  In fact the length-`d` rectangle uses both coatom targets and both
physical cells, so both participate in the compiler matching.

Consequently "only the first occurrence carries the q1 mark" can mean only
an additional externally imposed marked-role ledger.  It cannot at the same
time be cited as a primitive physical provider transfer.  If that narrower
ledger is intended, Theorem 6.2 must say so explicitly and must not be fed
into a min-cut whose loads count literal available occurrences.

A physical q1-open companion can cancel the first `d-1` ray levels while
leaving the longest level unmatched.  But its own longest-cell change is
then a second q1 root.  It must be recorded as collateral and closed by
external redundancy or by a joint q1 flow.  This is the weakest honest
ray-twin interface; it does not prove a clean primitive full-deck root.

## 6. Audited conclusion

The same-neighbour calculation supplies the missing local mechanism:

\[
 \boxed{\text{one returned stutter/flag separator}
        +\text{ one private }d\text{-ray}
        \Longrightarrow\text{ one literal coatom augmenter}.}
\]

What is not supplied by the raw high rotor or by a full inverse twin is a
dimension-uniform bank of private rays.  The remaining all-dimensional
statement is therefore a guarded occurrence theorem: plant enough repeated
owner fibres whose `d` changed cells avoid (or augment through) one common
compiler matching.  Exact upper return is already automatic for these
fixed-neighbour fibres.

## 7. Reconciliation with the patched theorem

The patched theorem now makes the three audited distinctions literally:

* the positive site is an owner stutter with a returned exterior interface;
* its payload is a lower/compiler ray and its upper deck returns exactly;
* Theorems 6.2--6.3 use a private, occurrence-labelled capacity-one token
  path with an explicit ordered serial-compatibility row, while Proposition
  6.4 classifies a full inverse twin as zero-current.
* Proposition 6.5 records the cellwise telescoping law: returning the marked
  middle fibre state forces zero payload, so the stutter is not a reusable
  nonzero catalyst.

Accordingly the corrected note no longer claims a marked/unmarked inverse
twin as a physical primitive root.  The remaining supply hypothesis is
explicit and was not audited as an existence theorem.

## 8. Independent audit of the nonloop obstruction

The companion nonloop argument was checked independently as follows.

1. The labelled cross condition follows in both directions by comparing
   the two survivor differences; in the raw core/high pair, disjointness of
   the core newborn forces literal equality of every active flag cell.
2. A singleton oldest cell on a distinct-owner transition is exactly the
   deleted owner coordinate, so its coatom is the owner intersection.
3. Summing the edge identity
   `chi_X+chi_Y=chi_(X intersect Y)+chi_(X union Y)` gives the paired-current
   equation under separate in/out degree return.  Without return, the exact
   residual is `partial_r(Delta d^+ + Delta d^-)`.
4. Coverage is converted to upper occurrence return only in the exact-deck
   or protected-unique-deletion cases stated in the theorem.
5. After allowing shore transposition, the support-two primitive-lower
   rectangle is necessarily the displayed mixed star--top octahedron and
   carries the opposite upper primitive.

Verdict: `PASS_SCOPED_LABELLED_CROSS_STUTTER_RAY_AND_PAIRED_CURRENT`.
No literal age lift of the octahedron and no all-dimensional private-ray
supply is included in this verdict.

There is also a capacity distinction from a literally returned catalyst.
One stutter fibre contains one stateful provider occurrence.  After
`z -> z'` that occurrence remains at `Q_(z')`; it may continue moving the
same unit, but resetting it reverses the payload.  Consequently one site can
close at most one independent surplus-to-hole path at terminal time.  A bank
of `s` marked sites has net augmentation at most `s`.  The exterior
two-neighbour interface is returned, but the provider token is stateful and
consumable.  Hence projected strong connectivity cannot replace the
occurrence/time-expanded capacities required by the global flow.
