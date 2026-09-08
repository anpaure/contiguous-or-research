# The `0x4e63` phase corridor, named-blocker criterion, and exact sharp-third-port CNF

Date: 2026-07-30

Status: exact one-cell and sharp radius-two/radius-three theorems; exact
two-port obstruction; proof-safe fixed-support CNF construction.  No new
universal word is claimed.  The proof-log CNF portfolio has not been run
because H100 headroom has not been re-authorized.

## 1. Frozen five-phase word

Let

```text
C = scratch/k16_fivephase_rex_hole20067.word
SHA-256 eef3555aa12675de8707de994d20300aaf8e96538b4691880810d84454fbb1b5
```

The word has length `12874`.  Independent full replay gives the sole hole

\[
 E=\mathtt{4e63}.                                         \tag{1.1}
\]

Put

\[
 H=\mathtt{287d},\qquad A=\mathtt{a879}.                  \tag{1.2}
\]

The two physical phase ports are

\[
 p=6439,qquad t=12873.                                   \tag{1.3}
\]

Their exact collar is

\[
 C_{6438}=\mathtt{2879},\quad C_p=\mathtt{a069},\quad
 C_{12872}=\mathtt{4e61},\quad C_t=H.                    \tag{1.4}
\]

In `C`, `H` has the unique witness `[t,t]`, `A` has the unique witness
`[6438,p]`, and `E` is absent.

## 2. Complete one-cell census

Define the terminal phase cube

\[
 X=\{\mathtt{0002}\vee s:s\subseteq\mathtt{4e61}\},
 \qquad |X|=128.                                          \tag{2.1}
\]

### Theorem 2.1 (sharp `E -> H` transfer)

Among all `3,282,870=12874(2^8-1)` substitutions by nonzero submasks of
`E`, exactly `26,916` create an `E` witness.  None is universal.  The
minimum collateral is one and is attained exactly by

\[
                C_t:H\longmapsto x,qquad x\in X.          \tag{2.2}
\]

Every word in (2.2) has sole hole `H`.

#### Proof

Any new `E` witness contains the changed cell, so its replacement must be a
submask of `E`; hence the `3,282,870` rows are exhaustive.  The exact
suffix/prefix multiplicity recurrence removes every old crossing interval,
adds every new crossing interval, and records the resulting hole set.  Its
authenticated census gives the stated totals and the exact 128-row cube.
Locally,

\[
                  \mathtt{4e61}\vee x=E\qquad(x\in X),    \tag{2.3}
\]

so `[12872,t]` supplies `E`, while replacing the unique singleton `H`
removes `H`. \(\square\)

The complete debt-count distribution among the 26,916 service rows is
retained in the audit; in particular there is no omitted debt-zero row.

## 3. All 128 exact return frontiers

Define the central low cube

\[
 Y=\{\mathtt{2004}\vee r:r\subseteq\mathtt{0069}\},
 \qquad |Y|=16.                                           \tag{3.1}
\]

### Theorem 3.1 (complete first-return graph)

For every `x in X`, start from `C[t<-x]`, whose sole hole is `H`.  A separate
complete one-cell census gives, identically for all 128 states:

\[
\begin{array}{c|r}
\text{service substitutions}&26783\\
\text{universal substitutions}&0\\
\text{minimum collateral}&1\\
\text{minimum rows}&17.
\end{array}                                               \tag{3.2}
\]

The 17 minimum rows are exactly

\[
\begin{array}{rcl}
t:x&\longmapsto&H,\qquad\text{new sole hole }E;\\
p:\mathtt{a069}&\longmapsto&y\in Y,
   \qquad\text{new sole hole }A.
\end{array}                                               \tag{3.3}
\]

Thus the new label enters the exact minimum-debt graph as

\[
                     E\longrightarrow H
                     \longrightarrow\{E,A\},              \tag{3.4}
\]

and no first return reaches zero or a fourth one-hole label.

#### Proof

Each of the 128 overridden words was rebuilt independently, checked to have
sole hole `H`, and subjected to all `3,282,870` return assignments.  All
reports have status `PASS_EXACT_NO_DEBT_FREE_RETURN`.  Their aggregate has
`3,428,224` service rows and `2,176` minimum rows.  The fail-closed manifest
audit checks every file, the retained semantic-source and frozen-binary
hashes, the 128-value domain, and the transition sets (3.3).  It explicitly
does not claim that the retained first source is the byte-exact build source;
the independently frozen radius-two audit supplies the stronger lineage.
\(\square\)

The 128 nonminimum debt histograms split into 36 classes, so Theorem 3.1 is
not inferred from superficial byte equality.

## 4. The complete sharp third layer

Define the high central cube

\[
 Z=\{\mathtt{a000}\vee r:r\subseteq\mathtt{0069}\},
 \qquad |Z|=16;                                           \tag{4.1}
\]
the original value `0xa069` belongs to `Z`.

For every `(x,y) in X times Y`, let `Q_(y,x)` be obtained by the sharp
terminal edit `H->x` and the sharp central edit `0xa069->y`.  Every one of
these `128*16=2048` physical words has sole hole `A`.  The complete next
one-cell census of every state gives:

1. no universal row;
2. minimum collateral one;
3. exactly seventeen minimum rows;
4. sixteen central returns `y->z`, `z in Z`, each leaving sole hole `H`;
5. one terminal move `x->A`, leaving sole hole `E`.

Hence, with every coordinate outside `{p,t}` frozen, the authenticated sharp
service subfibre has label transitions

\[
 E\longrightarrow H\longrightarrow A
 \longrightarrow\{H,E\},                                 \tag{4.2}
\]

together with the terminal inverse `H->E`.  No zero-debt row and no fourth
one-hole label occurs on this complete sharp radius-three fibre.  The exact
certificate is

```text
scratch/k16_fivephase_radius3_sharp_fibre_exact_20260730.audit.json
SHA-256 b164a2067d03fc968659ba89bf9c41b3fae242d81bbecb865651944b33efb629
```

It records `2048` distinct interval-multiplicity fingerprints, so the result
is not a quotient by the current hole label.  This theorem does not classify
states reached after a higher-collateral edit or a hole-neutral edit outside
the two named ports.

## 5. Exact two-port obstruction

### Theorem 5.1 (two phase cells cannot close)

Freeze every cell except `p` and `t`.  No pair of nonzero replacement values
at those two positions covers `E,H,A` simultaneously.  In particular no
universal word exists on this unrestricted two-port fibre.

#### Proof

Any new `E` witness must use `p` or `t`, since `E` is absent in the frozen
word.  If it uses `t`, then `t` cannot simultaneously be the singleton `H`
or `A`; every longer interval ending at `t` contains `0x4e61`, which has
bits outside both `H` and `A`.  Thus `p` would have to supply both `H` and
`A`.  Near `p`, an exact `H` witness requires bit `0x0004` and forbids bit
`0x8000`, whereas an exact `A` witness requires `0x8000` and forbids
`0x0004`.  One value cannot do both.

If the new `E` witness instead uses `p`, the exact suffix/prefix catalogue at
`p` has only the empty side-context contained in `E`.  Hence `p` itself must
equal `E`, and no interval through `p` can then equal `H` or `A`; `t` would
have to supply both.  At `t`, `H` and `A` can only be singleton witnesses,
and one cell cannot equal both.  An interval meeting both ports crosses a
fixed gap of OR `0xffff`, so it cannot equal any proper target. \(\square\)

Thus any completion requires at least one coordinate outside `{p,t}`.

## 6. Named-blocker witness criterion

The finite objective can be stated without aggregate hole minimization.

### Lemma 6.1 (one-casualty portal iff)

Let `U` have sole hole `B`.  Suppose that after replacing `U_p` by `v`, `B`
is covered and every target except possibly `D` is covered.  Then the
replaced word is universal if and only if `D` is covered.  Any such `D`
witness is either an unchanged interval avoiding `p` or a new interval
through `p`.

#### Proof

This is exactly the stated partition of the coverage equations. \(\square\)

Applied to the two authenticated basins:

* In the append-`0200` word, each sharp central portal fills `H` and destroys
  only `A`.  It closes immediately once `A=0xa879` has a second witness not
  destroyed by the central portal.
* In the five-phase word `C`, each sharp terminal portal fills `E` and
  destroys only the unique terminal `H`.  It closes immediately once
  `H=0x287d` has a second nonterminal witness.

The first exact nonterminal `H` prices are the 16 central rows `p->Y`; every
one creates `H` but removes `A`.  Thus five-phase rex converts the named
blocker from `H` to `A`; it does not discharge it.  This is the correct
Hall/annealing objective: buy one compatible backup witness, not a smaller
undifferentiated singleton count.  A packet buying that witness must also
preserve every other target and the portal service; an isolated second
witness is not by itself sufficient.

The exact nonterminal prepayment census considers every nonterminal position
and every nonzero replacement capable of creating `H`.  It has `27,036`
service rows, no coverage-safe row, and collateral floor one at exactly the
16 central rows, all of which lose `A`.  Therefore no single precursor edit
backs up `H`.  Independently, Section 4 proves that no single third edit
closes the authenticated terminal-plus-central sharp fibre.  The retained
audit is

```text
scratch/k16_fivephase_named_blocker_20260730.audit.json
SHA-256 d19f4415031b0db44bd3faaed011b609c79b1fab1c53e958f4bcce577179fd19
```

The authenticated unrestricted append-phase collar model reinforces this
boundary.  It allows arbitrary nonzero replacements at
`{0,1,6439,6440,6441,12873}` in the append-`0200` source, retains only 17
residual targets and 285 exact interval forms, and its CP-SAT diagnostic
reports `INFEASIBLE`.  Because the retained JSON has no checked DRAT/LRAT
proof and incomplete driver lineage, this is computational evidence for that
six-cell model, not a solver-independent no-go.  We therefore do not claim
that collar closed: a proof-producing search must either certify this face or
recruit an outside cell/global coherent exchange.  The source-relative
diagnostic artifact is

```text
scratch/k16_append0200_phase_collar_csp_20260730.audit.json
SHA-256 20cbfa5ef4bfe51f288db864fcedb224bdff99ac12064ca49ab10d20f8fce069
```

## 7. Exact fixed-support CNF

Let `P={p_1<...<p_s}`, `s<=3`, be a proposed replacement support and split
`C\P` into fixed consecutive segments `J_0,...,J_s`.  Let

\[
 K(P)=\{m\ne0:\text{no witness of }m\text{ lies wholly in one }J_i\}.       \tag{7.1}
\]

Targets outside `K(P)` retain an unchanged witness.  An interval meeting
the consecutive support block `p_a,...,p_b` has exact OR

\[
 f\vee x_a\vee\cdots\vee x_b,                              \tag{7.2}
\]

where `f` is a left suffix OR, all complete fixed gaps between the support
positions, and a right prefix OR.  These are all possible changed intervals.
Since each endpoint chain has at most 17 states,

\[
                         |K(P)|\le1+289s\le868.             \tag{7.3}
\]

Indeed, every `m in K(P)` other than the original hole `E` has an interval
witness in `C` meeting at least one member of `P`.  Charge it to the first
support position met by such a witness.  Its label is one of at most
`17*17=289` original left-suffix/right-prefix OR pairs at that position;
adding `E` proves (7.3).

Give each support cell sixteen bit variables and require it to be nonzero,
in addition to any declared domain constraints.  For every `m in K(P)` and
every form (7.2) with `f subseteq m`, introduce a witness variable.  Its
implications forbid every value bit outside `m` and require every bit of
`m\f` in at least one involved support cell.  Requiring one witness variable
per target is necessary and sufficient for literal universality.  This is an
exact Tseitin encoding, not a relaxation.

### Sharp third-port branch

For each `q notin {6439,12873}`, the proof-producing branch uses

\[
\begin{aligned}
x_{12873}&=\mathtt{0002}\vee s,&&s\subseteq\mathtt{4e61},\\
x_{6439}&=\mathtt{2004}\vee r,&&r\subseteq\mathtt{0069},\\
0\ne x_q&\subseteq A.
\end{aligned}                                               \tag{7.4}
\]

The last restriction is exact because the authenticated two-port cube state
has sole hole `A`; a third-cell witness of `A` must use a nonzero submask of
`A`.  There are exactly `12872` third-position branches.  The exact census of
Section 4 has already proved that all these branches are nonuniversal.  A
checked UNSAT proof for each CNF would provide a proof-log strengthening of
that authenticated census.  Neither result excludes higher-collateral first
portals or a cooperative witness packet outside the sharp fibre.

The exact builder and fail-closed SAT decoder are:

```text
scratch/build_threadA_k16_rex20067_sharp_third_port_cnf_20260730.py
scratch/decode_threadA_k16_rex20067_sharp_third_port_sat_20260730.py
```

The builder pins the source and the independently audited radius-two and
radius-three prerequisite hashes.  A SAT model is
accepted only after full 65,535-target replay; UNSAT requires a checked
DRAT/LRAT proof; timeouts and resource exits are `UNKNOWN`.  No H100 portfolio
was launched in this turn.

The separate literal face

```text
scratch/root_k16_fivephase_hole20067_hamming1_support55_20260730.positions.txt
SHA-256 16bf51eb5a7351cbc86346378b68233fdffbf8957811871b40e4ebf6545c7502
```

contains 55 positions.  Exhausting its
`C(55,1)+C(55,2)+C(55,3)=27775` supports would prove only that listed face,
not a global radius-three theorem.

## 8. Verified boundary

No new universal word was found.  The exact current conclusion is:

* no one-cell completion of `C`;
* no two-cell completion passing through any of its 128 minimum first
  portals;
* no three-cell completion passing first through a sharp terminal portal and
  then through a sharp central portal;
* no completion using only the two named phase ports;
* no new one-hole label beyond `{E,H,A}` on the authenticated sharp
  radius-three fibre;
* exact proof-producing CNFs are ready but the DRAT/LRAT portfolio is unrun.

Therefore the global bracket remains

\[
                         12873\le\nu(16)\le12875.           \tag{8.1}
\]

## 9. Frozen artifacts

```text
scratch/audit_threadA_k16_rex20067_return_bundle_20260730.py
  SHA-256 a91da786cf5d44510792a42bf00e017e5dca6d69bcf7820227cd258463ea14dd

scratch/threadA_k16_rex20067_return_bundle_20260730.audit.json
  SHA-256 1e3d4c1e7e8dabe45cc2ec6fccca4341642be99cf693a461ea4354b8fa9997f0
  (data/replay audit; the retained first C++ file is only a semantic
   ancestor of the frozen executable, so this artifact does not claim a
   source-to-binary rebuild chain)

scratch/threadA_k16_rex20067_return_census_20260730/first_census.audit.json
  SHA-256 dc33f876461d8e5c064cec31ff1e1e89fce79610272920a3dd600dbee86b95fd

128 return JSONs, path-independent aggregate SHA-256
  3bd19250269b0d96e156422a6612ea639d3f47e701c6eccc1f4365fb40360465

scratch/k16_fivephase_radius2_exact_20260730.audit.json
  SHA-256 042e4a09e51d48990f43297492dea8cd3b24e7b928605910ecb10a0dec4e7a99

scratch/k16_fivephase_radius3_sharp_fibre_exact_20260730.audit.json
  SHA-256 b164a2067d03fc968659ba89bf9c41b3fae242d81bbecb865651944b33efb629

scratch/r_k16_fivephase_named_blocker_20260730.audit.json
  SHA-256 9f892c40179a09bbe8c6c73ad05f18153797c8ad55519ac8451326daa1d1dac5

scratch/build_threadA_k16_rex20067_sharp_third_port_cnf_20260730.py
  SHA-256 94042d2c9d912376772df490b37d71b60ecb6181b302b1a884d0cb6cd35a3236

scratch/decode_threadA_k16_rex20067_sharp_third_port_sat_20260730.py
  SHA-256 ce2a455532375ed4b98a363773d8f9c269063e8da3a0a2f6a01b4cfe2fa37f08
```
