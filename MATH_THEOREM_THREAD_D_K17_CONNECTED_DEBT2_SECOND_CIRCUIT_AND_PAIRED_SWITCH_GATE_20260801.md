# Thread D: the connected `k=17` debt-two factor—second-circuit parity, overlap terms, and paired-switch gate

Date: 2026-08-01  
Status: exact theorem on the frozen post-`C16` factor, exhaustive full
single-`H` census through bipartite support `C14`, exact service-conditioned
`D/H` census through support `C22`, and independent literal replay.  The
finite census concerns only quotient topology, `Z17` voltage, and the
immediate rank-10/rank-7 palettes.  It makes no claim about deeper shadows,
residence, or compilation.

## 0. Result

The frozen literal factor is

```text
scratch/threadD_k17_connected_debt2_repair_20260801/
  seed17931.minimum_debt_assignment_cycle.factor.tsv
SHA256 c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587
```

It consists of perfect incidence matchings `D,H` on `N=1430` owner and
facet orbits.  Its quotient permutation

\[
                         \pi=H^{-1}D                         \tag{0.1}
\]

is one `1430`-cycle, its physical voltage is `9 mod 17`, its rank-10 upper
palette is exact, and its lower palette has precisely the two holes

\[
                         a=0x00e0f,\qquad b=0x01547.          \tag{0.2}
\]

The exact load histograms are

\[
 \mu_{10}:1^{878}2^{247}3^{18}4^1,
 \qquad
 \mu_7:0^2 1^{874}2^{249}3^{18}4^1.             \tag{0.2a}
\]

It was obtained from the complement-dual two-component factor by the
`H`-assignment cycle

\[
 \sigma=(425,395,396,665,650,608,157,135),                  \tag{0.3}
\]

whose eight assignment rows form a literal bipartite `C16`.

For a second **single `H` assignment circuit** of assignment length `t`, the
following are necessary and sufficient:

1. all `t` crossed literal incidences exist and remain disjoint from `D`;
2. `\sigma_t^{-1}\pi` is one quotient cycle;
3. its direct `Z17` voltage is nonzero;
4. the exact loss/gain inequality (2.5) holds for every upper and lower
   target.

Since `N` is even and both the old and desired permutations are Hamilton,
`t` must be odd.  The current `H` matching has no parallel one-row move, so
the theoretical minimum is `t=3`, a bipartite `C6`.

The complete current-factor censuses give:

| assignment length `t` | bipartite circuit | geometric | edge-disjoint | connected | nonzero voltage | upper exact | both palettes exact | minimum total debt |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | `C6`  | 621 | 387 | 172 | 170 | 23  | 0 | 2 |
| 5 | `C10` | 8,045 | 4,123 | 1,465 | 1,404 | 37 | 0 | 3 |
| 7 | `C14` | 303,975 | 118,902 | 30,435 | 28,859 | 211 | 0 | 2 |

A separate exact service-conditioned census covers both the `D` and `H`
sides.  It is complete for repairs because every repair must contain a
provider for each hole in (0.2).  Through assignment support `11`, it finds
`68,456` simple one-side circuits that gain both holes, of which `8,073`
are connected with nonzero voltage, but none preserves both terminal
palettes.  Consequently the first unclosed **single one-side circuit** shell
on this factor is assignment length `13`, i.e. bipartite `C26`.  This does
not exclude two simultaneous circuits or a genuinely paired `D/H` move.

The last two odd shells on each side have the exact profile

| side | `t` | targeted circuits | connected, nonzero | upper-safe | lower-safe | both-safe | minimum total debt |
|:---:|---:|---:|---:|---:|---:|---:|---:|
| `H` | 9  | 851    | 82    | 0 | 0 | 0 | 4 |
| `H` | 11 | 41,704 | 4,170 | 4 | 0 | 0 | 4 |
| `D` | 9  | 504    | 100   | 0 | 1 | 0 | 3 |
| `D` | 11 | 25,160 | 3,714 | 2 | 9 | 0 | 3 |

There is one selected parallel atom on the `D` side,

\[
                 3825\longrightarrow3829
                 \quad\text{at }(owner,facet)=(425,295).       \tag{0.4}
\]

It preserves quotient endpoints but sends voltage `9` to `0`, changes the
lower ticket `0x00787 -> 0x00d0f`, and changes the upper ticket
`0x01e9f -> 0x01f4f`.  In particular it repairs neither hole in (0.2) and
is not itself a physical terminal solution.  It may still participate in a
compound move because overlap terms can change these tickets again.

## 1. Literal matching notation

Let `O` be the owner orbit set, `F` the facet orbit set, and let

\[
                         d,h:O\longrightarrow F               \tag{1.1}
\]

be the endpoint maps of the two perfect matchings.  Each endpoint pair also
carries a literal incidence label and hence a `Z17` shift.  Endpoint maps
alone therefore determine quotient topology but not physical voltage or
turn colours.

For owner `x`, let

\[
 L_{d,h}(x)=\operatorname{can}
   \bigl(\operatorname{facet}(d_x)\cap\operatorname{facet}(h_x)\bigr)       \tag{1.2}
\]

be the rank-seven lower turn, with both facets put into the physical owner
gauge.  For facet `f`, let

\[
 U_{d,h}(f)=\operatorname{can}
   \bigl(\operatorname{owner}(d^f)\cup\operatorname{owner}(h^f)\bigr)       \tag{1.3}
\]

be the rank-ten upper turn, with both owners put into the physical facet
gauge.  Here `d_x,h_x` denote edges at an owner and `d^f,h^f` edges at a
facet.  These definitions include literal phase labels; replacing a
parallel edge can change (1.2) or (1.3) without changing `d` or `h` as
endpoint maps.

Write `mu_-(T),mu_+(T)` for the present lower and upper multiplicities.

## 2. Exact one-side circuit theorem

Choose distinct owners `x_0,...,x_(t-1)`, put

\[
              \tau=(x_0\ x_1\ \cdots\ x_{t-1}),\qquad
              f_i=h(x_i),                                      \tag{2.1}
\]

and seek a literal incidence `e_i` from `x_i` to `f_(i+1)`, with indices
cyclic.  Replacing `h_{x_i}` by `e_i` gives endpoint map

\[
                         h'=h\tau.                              \tag{2.2}
\]

### Theorem 2.1 (necessary and sufficient terminal test)

The replacement is an upper/lower-exact physical Hamilton factor if and
only if all four conditions below hold.

1. **Literal matching.**  Every `e_i` exists, the new edges are distinct,
   and `e_i` is not the selected `D` edge at `x_i`.
2. **Quotient topology.**
   \[
                         \pi'=\tau^{-1}\pi                     \tag{2.3}
   \]
   is one cycle.
3. **Physical lift.**  If `s(e)` is the stored incidence shift, then
   \[
      V'=V+\sum_i s(h_{x_i})-\sum_i s(e_i)\not\equiv0\pmod {17}.             \tag{2.4}
   \]
4. **Both palettes.**  For each shore `epsilon in {-,+}` and target `T`,
   \[
       \mu_\epsilon(T)-\ell_\epsilon(T)+g_\epsilon(T)\ge1.                  \tag{2.5}
   \]
   The lower deleted and added tickets are respectively
   \[
                  L_{d,h}(x_i),\qquad L_{d,h'}(x_i),                         \tag{2.6}
   \]
   while at facet `f_i` the upper deleted and added tickets are
   \[
                  U_{d,h}(f_i),\qquad
                  U_{d,h'}(f_i)=U(d^{f_i},e_{i-1}).                          \tag{2.7}
   \]

#### Proof

The crossed endpoints in (2.1) use every selected owner and every selected
old facet once, so condition 1 is exactly perfectness and `D/H`
edge-disjointness.  Inverting (2.2) gives (2.3), hence condition 2 is exactly
quotient connectedness.  Traversing the alternating factor changes only the
displayed `H` shifts, giving (2.4); a connected quotient cycle lifts to one
physical cycle exactly when this voltage is nonzero.  Finally, only the
owner turns (2.6) and facet turns (2.7) change.  Subtracting their deleted
indicators and adding their new indicators gives (2.5), which is plainly
equivalent to positive final multiplicity for every target.  These four
conditions are therefore necessary and sufficient.  \(\square\)

Since `mu_-(a)=mu_-(b)=0` in the current factor, (2.5) immediately implies

\[
                         \{a,b\}\subseteq
              \{L_{d,h'}(x_i):0\le i<t\}.                     \tag{2.8}
\]

Equivalently, the complete current palette demand is the integer cone

\[
\begin{aligned}
 \Delta_7(a),\Delta_7(b)&\ge1,\\
 \Delta_7(T)&\ge1-\mu_7(T) &&(T\ne a,b),\\
 \Delta_{10}(T)&\ge1-\mu_{10}(T) &&(\text{all rank-ten }T),\\
 \sum_T\Delta_7(T)&=\sum_T\Delta_{10}(T)=0.          \tag{2.9}
\end{aligned}
\]

Thus a repair must consume exactly two **net** lower repeat units: the total
load remains `1430` while the number of covered lower colours rises from
`1142` to `1144`.  This is stronger than merely creating the two holes;
every load-one colour lost by the circuit must be recreated in the same
terminal packet.

Thus a provider-first census loses no solutions if it first insists that
the new lower tickets contain both named holes.

## 3. Parity and the sharp first shell

A cycle of length `t` has sign `(-1)^(t-1)`.  A Hamilton permutation on the
even set of `1430` owners has sign `-1`.  If both `pi` and `tau^{-1}pi` are
Hamilton, then

\[
       -1=\operatorname{sgn}(\tau^{-1}\pi)
          =(-1)^{t-1}(-1),                                    \tag{3.1}
\]

so `t` is odd.

The topology test itself compresses to `t` points.  List the selected owners
as `v_0,...,v_(t-1)` in their cyclic order on the current Hamilton cycle,
write `tau(v_j)=v_(alpha(j))`, and put `s(j)=j+1 mod t`.  Contracting the
unchanged Hamilton segments between successive selected owners gives

\[
  c(\tau^{-1}\pi)=c(\alpha^{-1}s) \quad\text{for an `H` circuit},          \tag{3.2}
\]

and, for a `D` circuit with endpoint permutation `tau`,

\[
  c(\pi\tau)=c(s\alpha).                                                   \tag{3.3}
\]

Indeed, at the end of old segment `j`, left multiplication by
`tau^{-1}` sends the old successor `v_(j+1)` to
`v_(alpha^{-1}(j+1))`; right multiplication makes the segment entered from
`v_j` the old segment following `v_(alpha(j))`.  Thus the displayed
permutations are the exact contracted successor maps.  In particular, the
one-cycle requirement in Theorem 2.1 can be checked on `t` symbols; parity
is only its coarsest consequence.

There are only two apparent exceptions.

* `t=1` can change a literal incidence only when the currently selected
  owner-facet pair has a parallel label.  The current `H` matching selects
  none of the eight doubled quotient pairs, so this exception is absent.
* `t=2` would be a physical `C4`.  It is already ruled out by (3.1), and
  independently the Boolean rank-eight/rank-nine incidence graph has no
  simple `C4`.

Hence `t=3` (`C6`) is the exact theoretical minimum for a nontrivial
one-sided endpoint circuit.  The full `H` audit in Section 6 closes
`t=3,5,7`; the service-conditioned `D/H` audit then closes every
repair-capable one-side circuit through `t=11`.  Thus `t=13` (`C26`) is the
first untested single one-side circuit.  The last statement is deliberately
not a claim about an arbitrary even permutation of several disjoint cycles.

## 4. Exact overlap term after the first `C16`

Let `h_0` be the complement-dual matching before (0.3).  The current
matching is

\[
                         h_1=h_0\sigma.                         \tag{4.1}
\]

If a second current-relative circuit is `tau`, then

\[
                 h_2=h_1\tau=h_0\sigma\tau,qquad
                 \pi_2=\tau^{-1}\pi_1.                        \tag{4.2}
\]

Equation (4.2), not a union of the two support sets, is the exact topology.
At owner `x` the final endpoint is

\[
                         h_0(\sigma\tau(x)).                    \tag{4.3}
\]

Thus an overlap can restore an original row, cancel a first-stage row, or
create a third mixed row.  The same issue occurs at upper facets through
the inverse permutation.

Here is an exact way to expose the cross term.  For a literal matching
state indexed by `gamma`, let `L_gamma(x),U_gamma(f)` be (1.2)--(1.3), and
let `[P]` denote the indicator of `P`.  If `tau` is incorrectly evaluated
as an isolated move from `h_0`, the missing lower correction is

\[
 C^-_T(\sigma,\tau)=\sum_{x\in O}
 \bigl([L_{\sigma\tau}(x)=T]-[L_\sigma(x)=T]
       -[L_\tau(x)=T]+[L_0(x)=T]\bigr),                         \tag{4.4}
\]

and the upper correction is

\[
 C^+_T(\sigma,\tau)=\sum_{f\in F}
 \bigl([U_{\sigma\tau}(f)=T]-[U_\sigma(f)=T]
       -[U_\tau(f)=T]+[U_0(f)=T]\bigr).                        \tag{4.5}
\]

The analogous voltage correction is

\[
 C_V=V_{\sigma\tau}-V_\sigma-V_\tau+V_0.                      \tag{4.6}
\]

These corrections vanish for disjoint assignment supports with disjoint
literal phase choices.  They need not vanish when the cycles overlap.
Equivalently, one may avoid (4.4)--(4.6) entirely by applying Theorem 2.1
to the **current** factor `h_1`; current-relative losses and gains then
already contain every cross term.  This is the fail-closed rule used by the
finite census.

## 5. Paired `D/H` switches are a different object

Let endpoint permutations `alpha,beta` and literal phase choices define

\[
                         d'=d\alpha,\qquad h'=h\beta.            \tag{5.1}
\]

Then

\[
                         \pi'=\beta^{-1}\pi\alpha.              \tag{5.2}
\]

### Theorem 5.1 (paired exact criterion)

A paired move is a physical, palette-exact Hamilton factor if and only if

1. the chosen literal `D'` and `H'` edges are two disjoint perfect
   matchings;
2. the permutation in (5.2) is one cycle;
3. its direct alternating voltage is nonzero; and
4. the final turns `L_(d',h')(x)` and `U_(d',h')(f)` satisfy the same load
   inequalities (2.5).

In particular, owner and facet locations where both sides change must be
recomputed as one turn.  Adding an isolated `D` ledger to an isolated `H`
ledger is unsound on such overlaps.

#### Proof

Perfectness gives (5.1); inversion gives (5.2).  Conditions 2 and 3 are
respectively quotient and physical connectedness.  The final palette is,
by definition, the multiset of the displayed final owner and facet turns,
so condition 4 is necessary and sufficient.  \(\square\)

Taking signs in (5.2), Hamilton-to-Hamilton requires

\[
                    \operatorname{sgn}(\alpha)
                    \operatorname{sgn}(\beta)=1.               \tag{5.3}
\]

For one `D` cycle of length `p` and one `H` cycle of length `q`, (5.3) is
equivalent to

\[
                              p+q\equiv0\pmod2.                 \tag{5.4}
\]

This is only a parity test, not a topology theorem.  With no parallel phase
atoms, the smallest simple paired Boolean move is `C6+C6` (`p=q=3`), since
the incidence graph has no simple `C4`.  On the present factor there is the
single `D` phase atom (0.4); it has `alpha=id`, so it can accompany an
`H-C6` without changing the sign test.  However, it has zero terminal
voltage and supplies neither current hole in isolation.  Any use of it must
therefore be audited jointly by Theorem 5.1, especially if the `H` circuit
touches owner `425` or facet `295`.

The smallest current move classes not closed by the combined audits are
therefore:

* an `H-C6` coupled to the unique `D` phase atom;
* a paired `D-C6/H-C6`;
* a compound even permutation such as two `H-C6` circuits; or
* the next single one-side circuit, `C26`.

## 6. Finite certificates and scope

The exhaustive current-factor enumerator is

```text
scratch/audit_threadD_k17_connected_debt2_second_circuits_20260801.cpp
SHA256 88349ffcecc747f6a9b8f931c615f9c243df3ba4a58bc0a4a4f32d14a7987f11
```

It reads both literal matchings from the post-`C16` factor; it does not
reconstruct `H=C(D)`.  It retains parallel incidence labels, removes only
cyclic rotations, and directly replays matching, topology, voltage, and both
palettes.  The H100 runs used one process.  The final service-conditioned
run had a `2 GiB` address-space cap and used only `11,264 KiB` maximum RSS.

The result hashes are:

```text
C6 audit   fecc45780e7bd7e711a06a339d6892a2611839efe73906a2e8103ab21381ab5a
C6 table   3d1ac8b37ed3883836fa2e3459516e2ba8b863d4685acc9d18b05881d5c5611c
C10 audit  8947c22e6e2eef19b58cbfd13ed8b940e3fef88d9588421343ae868d96780d24
C10 table  9917f76a4840a14d4df20fad8f12857dc54f2f6f33a0968d53c93ff61c99aa27
C14 audit  b8ee63ef4983eae338ebabd295360a2af8b7452e70d9ffb354ef02d10c7b5210
C14 table  ddef24f0f20203bad45f921b922b3fbedd843b8343089f634f4586d89818342d
```

An independent Python implementation rebuilds the full incidence atlas and
literal factor, replays every emitted minimum-debt row, and exhausts the
one-row parallel pairs:

```text
scratch/audit_threadD_k17_connected_debt2_second_circuits_independent_20260801.py
SHA256 bdb3a36b2ec5133438bef21a3d051c234d237149d72447474d8726b1338d2a1a

scratch/threadD_k17_connected_debt2_repair_20260801/
  second_circuits_independent.audit.json
SHA256 b9e59b48f319e64939ec65b43568cc44ed2f88a2d17e81df827286432f74138e
```

That replay certifies the base `(1430; voltage 9; upper debt 0; lower debt
2)`, all recorded C6/C10/C14 minimizers, all eight doubled quotient pairs,
the absence of an `H` phase atom, and the exact `D` atom ledger (0.4).
Exhaustiveness of the cycle counts belongs to the C++ enumerator; the Python
audit independently certifies the literal decoding and reported witnesses.

The final service-conditioned census is

```text
scratch/threadD_k17_connected_debt2_repair_20260801/
  second_final.catalogue.source.cpp
SHA256 f3599e0a83f1aa2f51d99a914222be6c154a9bbb48bbdd46961dabc2d3cea939

  second_final.second_circuits_B.audit.json
SHA256 936dfd01dc7c3f44a44536ca518a0a8bf56e034e885f30d175d47f6a5e25b499

  second_final.second_circuits_B_summary.tsv
SHA256 c40db77b5a0523cddf2c631350886e277150dfdb11b2fd67af41be66f73382d7

  second_final.second_circuits_B.tsv
SHA256 deb43e32d78ffe7de4d2a98d053ba79cbcb4727f9468a3e518e1301c76686247
```

It enumerates every simple `D`- or `H`-side assignment circuit of supports
`3,4,5,6,7,8,9,11` that gains both named holes.  Supports `10,12` are
excluded by the proved Hamilton parity law; smaller even supports are also
topologically ineligible, although retained in the diagnostic interface.
Every exact repair gains both holes, so the no-go through support `11` is
complete despite not enumerating circuits irrelevant to (0.2).  Its exact
totals are `68,456` targeted circuits, `8,073` connected nonzero-voltage
rows, and zero terminal two-palette survivors.

Every emitted connected row was then replayed by a second implementation
which imports no generator code:

```text
scratch/audit_threadD_k17_second_final_allrows_20260801.py
SHA256 3029fd752674de0363f58158ec17905a1724e903ac70b4295a0dbca3e15c4410

scratch/threadD_k17_connected_debt2_repair_20260801/
  independent_allrows.audit.json
SHA256 6908ef90d68dcd28d54feb848d8f23b2b87fc8dccddad4ef07e22cf706cdaea4
```

It independently reconstructs the atlas and base factor and recomputes all
`2,860` turns for each of the `8,073` rows.  All rows lift to one physical
cycle of length `24,310`; six are upper-exact, ten are lower-exact, and their
intersection is empty.  Runtime was `13.23 s`, with `53,376 KiB` maximum RSS
under a `2 GiB` H100 cap.  The nonemitted count `68,456` is certified by the
producer's hole-anchored enumeration and its completeness lemma, not by a
second enumeration.

## 7. Surviving sharp gate

For a single current one-side circuit, the exact provider-first gate is:

\[
 \boxed{
 \begin{array}{l}
 t\ge13\text{ odd};\quad \{0x00e0f,0x01547\}\subseteq
       \{L'_{x_i}\};\\
 \tau^{-1}\pi\text{ is one cycle};\quad V'\ne0;\\
 \mu_\pm-\ell_\pm+g_\pm\ge1\text{ targetwise}.
 \end{array}}                                                     \tag{7.1}
\]

For any mixed or compound packet, replace the first line's `t>=13` by the
appropriate support class, but retain (5.2) and recompute all final turns.
The determinant-free parity rule (5.3) is the only universal simplification;
overlap ledgers are genuinely nonlinear at the turn level.
