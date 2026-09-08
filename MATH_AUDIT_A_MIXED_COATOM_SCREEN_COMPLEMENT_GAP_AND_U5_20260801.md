# Mixed coatom screens: exact gap dual, two-polarity obstruction, and U5 correction

Date: 2026-08-01  
Lane: A, primary `B(k)+O(1)` packet audit  
Status: zero-owner-defect tensor independently verified; exact complement-gap
dual proved; simultaneous OR/AND transparency refuted; exact incidence-level
compiler criterion isolated.  No additive-constant theorem is claimed.

## 0. Verdict

The authoritative mixed-screen tensor is locally sound.  For every `d>=1`
and `r>=d+4`, the canonical union-screen set

\[
                              E=\{1,3,5,7\}                     \tag{0.1}
\]

gives two simple rank-`r` Johnson paths of length `12d+35` with the same
distinct owner set and endpoints, exact lower/upper q1 multisets, pointwise
equal prefix/suffix OR chains, equal internal OR support, equal clipped
positive-run boundary state, and internal positive-run floor `d+1`.
There is no owner sidecar.

The tensor is nevertheless one-polarity.

* Its prefix and suffix AND decks are incomparable in the two phases for
  every `d`.
* At `d=2`, even its internal AND supports differ.  This remains true for
  each of the three zero-owner-defect patterns.
* Literal complementation gives a simple **atom-gap tensor** with exact AND
  transparency and zero-run floor `d+1`, but the complementary tensor fails
  OR transparency and has singleton positive filler runs.

Thus the owner repair is closed, but a single mixed tensor does not supply a
simultaneous OR/AND, run/gap birail packet.  The remaining primary gates are
task/menu embedding, the incidence-level U5 compiler matching, and
regeneration.

## 1. The exact AND-deck replacement theorem

Fix a finite universe `Omega`.  For a nonempty word
`X=(X_1,...,X_h)`, define

\[
\begin{aligned}
 {cal P}_\cap(X)&=\{X_1\cap\cdots\cap X_j:1\le j\le h\},\\
 {cal S}_\cap(X)&=\{X_j\cap\cdots\cap X_h:1\le j\le h\},\\
 {cal I}_\cap(X)&=\{X_i\cap\cdots\cap X_j:1\le i\le j\le h\},\\
 T_\cap(X)&=\bigcap_{i=1}^hX_i.
\end{aligned}                                                   \tag{1.1}
\]

### Theorem 1.1 (linear AND transparency)

If

\[
\begin{gathered}
 {cal P}_\cap(X)\subseteq{cal P}_\cap(Y),\qquad
 {cal S}_\cap(X)\subseteq{cal S}_\cap(Y),\\
 {cal I}_\cap(X)\subseteq{cal I}_\cap(Y),\qquad
 T_\cap(X)=T_\cap(Y),
\end{gathered}                                                   \tag{1.2}
\]

then replacing `X` by `Y` in any linear exterior preserves every old
contiguous interval-intersection value.  Pairwise-disjoint replacements
compose.

#### Proof

Partition an old interval into the five cases: disjoint from the slot,
internal to it, crossing only the left boundary, crossing only the right
boundary, or crossing both.  Its slot contribution is respectively
unchanged, a member of `I_cap`, a member of `P_cap`, a member of `S_cap`, or
the total intersection.  Use (1.2) and intersect with the unchanged exterior
contribution.  The disjoint-slot composition proof is identical. \(\square\)

This is also immediate from De Morgan:

\[
             \bigcap_{i\in J}X_i
             =\Omega\setminus\bigcup_{i\in J}(\Omega\setminus X_i).
                                                                    \tag{1.3}
\]

For a proper cyclic carrier, put
`P^cap_0=S^cap_(h+1)=Omega` and define the separated two-ended deck

\[
 {cal J}^{\circ}_\cap(X)=
 \{P_i^\cap(X)\cap S_j^\cap(X):
     0\le i\le h, 1\le j\le h+1, i+1<j\}.                    \tag{1.4}
\]

If full-cycle intervals are forbidden, (1.2) together with
`J^o_cap(X) subseteq J^o_cap(Y)` is the context-independent sufficient
condition.  If the full cycle is allowed, separate prefix/suffix decks
suffice: overlapping or abutting chosen ends yield the total intersection,
which the full cycle realizes.  The strict gap in (1.4) is necessary by
complementing the three-cell OR counterexample.

AND decks do not control zero-run residence, multiplicity, width, addresses,
or compiler ownership.  Those remain separate boundary and incidence rows.

## 2. Independent audit of the zero-defect tensor

Use the active words

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab.
```

Let `A` be their six-coordinate active universe, put `n=d+2`, and take

\[
 F=\{f_0,\ldots,f_{n-1}\},\qquad C_i=F-\{f_i\},
 \qquad |K|=r-d-4.                                             \tag{2.1}
\]

The block for an active triple `V` is

\[
 B(V)=(K\cup V\cup C_0,\ldots,K\cup V\cup C_{n-1}).           \tag{2.2}
\]

At transition `j`, the lower and upper common neighbours are

\[
\begin{aligned}
 L_j&=K\cup(V_j\cap V_{j+1})\cup F,\\
 U_j&=K\cup(V_j\cup V_{j+1})\cup(F-\{f_0,f_{n-1}\}).
\end{aligned}                                                   \tag{2.3}
\]

Use `U_j` at (0.1) and `L_j` elsewhere.

### Theorem 2.1 (stress-test verdict)

The resulting two phases satisfy every local claim U1--U4 in the
authoritative tensor theorem.

#### Proof audit

Both screens in (2.3) have rank `r` and are Johnson-adjacent to the terminal
coatom of `B(V_j)` and the initial coatom of `B(V_(j+1))`.  Block, lower
screen and upper screen owners omit respectively one, zero and two fillers,
so types cannot collide.  On (0.1), the seven selected intersections and
four selected unions are separately distinct and have the same old/new
sets.  Thus every owner is distinct and the owner sets agree.

The first and last screens are lower.  They fill `F`, while an upper screen
advances the active prefix or suffix by exactly one contracted owner.
The base prefix/suffix OR chains agree, so the expanded chains agree
pointwise.  For internal ORs, first separate a singleton lower screen: its
seven possible values are common directly, because the seven selected
active intersections agree.  An interval meeting a lower screen and at
least one block cell has full filler and contracts to a consecutive active
interval.  After deleting the lower screens, each nontrivial component is
one block or a block--isolated-upper-screen--block triple.  Such an upper
screen has only the four filler states

\[
 F-\{f_0,f_{n-1}\},\quad F-\{f_0\},\quad
 F-\{f_{n-1}\},\quad F,                                      \tag{2.4}
\]

and depends only on its selected active union.  These four filler-profile
families are disjoint and exhaust the internal values.  Hence the exact
internal OR support is common and has size

\[
                          12n+7+12+25=12d+68.                   \tag{2.5}
\]

Active runs contain a complete `n`-block.  Middle fillers have connecting
run `n`; only `f_0,f_(n-1)` can also be absent at an isolated upper screen,
shortening the minimum to `n-1=d+1`.  The boundary blocks and filler schedule
are identical, giving equal clipped state.  Direct edge calculation gives
equal adjacent-intersection and adjacent-union multisets. \(\square\)

The proof in fact remains algebraically valid at `d=0`; the stated O(1)
application uses `d>=1`.

Inside the natural one-per-repeated-pair face, the three exact owner/OR/
residence patterns are

\[
\begin{array}{c|c|c}
\text{pattern}&\text{upper-screen positions}&\text{q1 multisets equal?}\\ \hline
0110&\{1,3,5,7\}&\text{yes}\\
1011&\{2,5,8,10\}&\text{yes}\\
1100&\{3,4,7,10\}&\text{no}.
\end{array}                                                     \tag{2.6}
\]

Thus the canonical root theorem correctly uses `0110`.  The broader
zero-defect theorem does not assert q1 exactness for every pattern.

## 3. Exact two-polarity obstruction

The mixed tensor does not preserve the AND boundary decks.  For the first
active row and all three patterns in (2.6), suppressing the common core gives

\[
\begin{array}{c|c|c}
 &\text{old-only}&\text{new-only}\\ \hline
 {cal P}_\cap&\{b,b\infty\}&\{a,a\infty\}\\
 {cal S}_\cap&\{eb\}&\{ea\}.
\end{array}                                                     \tag{3.1}
\]

Adding `K` to every displayed set gives the physical values.  Neither
directed deck inclusion holds, independently of `d`.

Unlike the older all-lower-screen walk, the zero-defect repair can also lose
**internal** AND support.  At `d=2`, `F={f_0,f_1,f_2,f_3}` and pattern
`0110`, the exact differences are

\[
\begin{aligned}
 {cal I}_\cap(X)\setminus{cal I}_\cap(Y)
  ={}&\{K\cup\{b,c,\infty,f_1\},
        K\cup\{a,c,\infty,f_2\}\},\\
 {cal I}_\cap(Y)\setminus{cal I}_\cap(X)
  ={}&\{K\cup\{a,c,\infty,f_1\},
        K\cup\{b,c,\infty,f_2\}\}.
\end{aligned}                                                   \tag{3.2}
\]

For the three rows, the three pattern-wise old-only/new-only counts at
`d=2` are respectively

\[
                             2/2,\qquad4/4,\qquad8/8.           \tag{3.3}
\]

This is a literal counterexample to simultaneous OR/AND-deck preservation.
The raw all-lower-screen tensor did preserve both internal supports, but it
had four repeated screen owners.  The mixed-screen repair removes that owner
defect while sacrificing internal AND transparency.  No owner sidecar
returns; rather, a new two-polarity profile would require a larger packet.

## 4. Exact complement/gap tensor

Embed the rank-`r` primal tensor in a `2r`-coordinate universe

\[
                    \Omega=K\mathbin{\dot\cup}A
                       \mathbin{\dot\cup}F\mathbin{\dot\cup}G,
                    \qquad |G|=r-4.                             \tag{4.1}
\]

Complement every primal owner in `Omega`.  The dual blocks and screens are

\[
\begin{aligned}
 B^\vee(V,i)&=G\cup(A\setminus V)\cup\{f_i\},\\
 L_j^\vee&=G\cup(A\setminus(V_j\cap V_{j+1})),\\
 U_j^\vee&=G\cup(A\setminus(V_j\cup V_{j+1}))
                         \cup\{f_0,f_{n-1}\}.
\end{aligned}                                                   \tag{4.2}
\]

### Theorem 4.1 (atom-gap dual)

With the canonical mixed-screen schedule (0.1), the dual phases are simple
rank-`r` Johnson paths with common endpoints and equal owner sets.  Their
pointwise prefix/suffix AND chains, internal AND supports and immediate
palettes agree.  Every internal zero-run has length at least `d+1`, with
equal clipped zero-run boundary state.

#### Proof

Complementation is an automorphism of `J(2r,r)` and a bijection on owners.
De Morgan sends every primal interval OR to the complementary dual interval
AND, proving all AND claims.  It swaps adjacent intersections and unions,
so the exact q1 multisets remain equal.  A dual zero-run is a primal
positive run, proving the residence assertion. \(\square\)

The dual is not OR-transparent.  Its OR boundary obstruction is the
complement of (3.1), and at `d=2` its internal OR support differs by the
complements of (3.2).  Moreover a middle filler occurs at exactly one cell
of each dual atom block and at no screen, so it has singleton positive runs.
Equivalently, the primal has singleton filler gaps.  Thus neither phase is
simultaneously positive-resident and gap-resident for threshold at least two.

The exact even/birail conclusion is therefore conditional: primal and dual
may serve separately guarded opposite-polarity rails, but one physical
chronology still needs a joint boundary/cross-rail theorem if both
semilattices or both residence signs are required at once.

## 5. Exact U5 correction: incidences, not cells

Let `H=(L,C;E)` be the compiler graph, and let `Phi` be the reachable macro
phase family.  Define the universally legal guarded-incidence set

\[
 E_{\rm all}=\{(\ell,c)\in E:
   (\ell,c)\text{ has a valid trace guard in every }\phi\in\Phi\}.
                                                                    \tag{5.1}
\]

The phasewise certificates may differ.  If one fixed literal certificate is
required, replace `E_all` by the smaller set on which that certificate is
phase-invariant; the same theorem applies to that explicitly stronger face.

Let `D_*` be the union of the cell ideals forbidden by all reachable
frontiers.  When a componentwise maximum `rho*` is used, one must verify

\[
                           D_*=\bigcup_\rho D(\rho)=D(\rho^*).   \tag{5.2}
\]

### Theorem 5.1 (exact common-compiler Hall criterion)

A common fixed compiler matching exists exactly when

\[
             |N_{E_{\rm all}}(X)\setminus D_*|\ge |X|
             \qquad\text{for every }X\subseteq L.              \tag{5.3}
\]

#### Proof

This is Hall's theorem in the universally legal incidence graph after
deleting `D_*`.  Every selected incidence has a valid trace guard in every
phase/frontier; conversely any common matching consists only of universally
legal incidences and avoids every forbidden ideal. \(\square\)

The coarser cell set

\[
 D_{\rm mac}=\{c:\text{some incidence at }c\text{ is not certified}\}
                                                                    \tag{5.4}
\]

gives a sufficient cell-deletion test
`delta_H(D(rho*) union D_mac)=0`.  It is necessary only on the explicitly
cell-deleted face, or when safety is cell-uniform.  It is not necessary for
the unrestricted compiler problem.  The minimal counterexample has safe
edges

\[
                              ac,\quad bd                         \tag{5.5}
\]

and one unsafe edge `bc`.  The safe common matching `{ac,bd}` uses cell `c`,
but (5.4) deletes `c` because of the unrelated unsafe incidence `bc` and
then falsely isolates `a`.

Thus U5 remains an exact Hall problem, but its correct atoms are guarded
target--cell incidences.  The scalar cell-deletion deficiency is a useful
stronger face, not a general necessity theorem.

## 6. Proved boundary and remaining gates

The mixed tensor unconditionally closes the local owner, q1, OR, positive-
residence and simple-topology rows for the canonical pattern.  The owner
sidecar is gone.

The exact remaining primary gates are:

1. embed the active six-label packet with an `Omega(m^2)` fixed-anchor menu
   after all physical exclusions;
2. prove the safe-incidence Hall system (5.3), or a bounded literal repair;
3. regenerate the same bounded interface through the Pascal lift; and
4. only for an even/birail construction demanding both polarities, supply a
   larger joint OR/AND and run/gap profile.

No K17 search and no asymptotic/additive-constant conclusion is used here.

## 7. Audit

Run

```bash
python3 scratch/audit_a_mixed_coatom_screen_or_and_gap_20260801.py
```

The audit independently reconstructs all three authenticated active rows,
all three exact mixed-screen patterns and every `1<=d<=12`.  It verifies the
owner/OR/residence claims, the q1 distinction in (2.6), the AND boundary
obstruction, the exact `d=2` internal differences, and the literal
`2r`-coordinate complement.  It also freezes the U5 counterexample.  The
all-`d` positive tensor theorem is symbolic; the finite range is an
independent replay, not its proof.

Frozen audit lineage:

* authoritative mixed theorem SHA-256
  `2d9fbf37ee6771013a28edd299b69ca5f4123c97d57f46339248e663fe6e2b83`;
* independent zero-defect/compiler theorem SHA-256
  `1d867afb6658c7724bc76f4760f85c3dccc1c0573d0459169358f929dbb2d415`;
* audit script SHA-256
  `cd6dd2d198e05308080ca0ee73ceea49ac24bbce721082e33521afd26788e68f`;
* audit JSON SHA-256
  `4d8d511971aa2b98dbbbf91f292203d651069cb88d31cbecd2ffe9d1e0b87c15`;
* canonical JSON payload
  `c325632a61f240fd544dd402b55ddb1b7bf3eacf4fe700a8fc3a37d9fdcdcb15`.

Three independent semantic audits separately passed Theorem 2.1, the
AND-deck/complement argument, and the mixed-screen internal-AND
counterexample.  The two older raw all-lower-screen notes are explicitly
scope-marked and are not provenance for the zero-defect claim.
