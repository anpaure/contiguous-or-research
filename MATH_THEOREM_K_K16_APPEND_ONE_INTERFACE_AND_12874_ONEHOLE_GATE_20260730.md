# K16 one-cell completion interfaces and the 12,874 one-hole gate

Date: 2026-07-30  
Lane: K  
Status: **proved the exact append/insertion/substitution criteria; proved
that the frozen length-12,873 prefix needs at least two appended cells and
admits no one-cell insertion; and completely audited all one-cell insertions
and substitutions of the new length-12,874 one-hole basin.  Every
substitution that installs the hole creates at least two casualties.  No
length-12,874 universal word is claimed.**

## 0. Current bracket

The authenticated partial word

```text
scratch/k16_12873_repaired_partial.word
SHA-256 0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6
```

has length 12,873 and holes

\[
H=\{0x287d,0xce61,0xce63\}.                           \tag{0.1}
\]

Appending

\[
x=0x0200,\qquad y=0x287d                              \tag{0.2}
\]

gives the verified universal word

```text
answers/k16_upper12875.word
SHA-256 d4690a0d11f1d8e69765ec988d9fbcbac63d354ebd6ab07aa8081b577a9ac0c9
```

of length 12,875.  Together with the proved counting lower bound,

\[
\boxed{12873\le\nu(16)\le12875}.                      \tag{0.3}
\]

The independent monotone ending-OR replay covers all 65,535 nonempty masks.
The three new witnesses, in zero-based positions of the completed word, are

\[
\begin{array}{c|c}
0x287d &[12874,12874],\\
0xce61 &[12871,12873],\\
0xce63 &[12870,12873].
\end{array}                                            \tag{0.4}

There is also an independently regenerated alternate completion

\[
w\Vert0x0661\Vert0x287d,                              \tag{0.5}
\]

of SHA-256
`b02da0f2a669068d698ed30aaa2009daaf67d3badaa8c3321e6e245478318d79`.
It is universal as well, but the retained canonical answer is (0.2).
\]

## 1. Exact one-append theorem

For a word \(w=(w_0,\ldots,w_{n-1})\), let

\[
\operatorname{Suff}(w)=
\{0,w_{n-1},w_{n-2}\vee w_{n-1},\ldots,
  w_0\vee\cdots\vee w_{n-1}\}                       \tag{1.1}
\]

and let \(\mathcal H(w)\) be its missing nonzero masks.

### Theorem 1.1 (append iff)

For a nonzero cell \(x\), the appended word \(w\Vert x\) is universal if
and only if

\[
\boxed{
\mathcal H(w)\subseteq
\{s\vee x:s\in\operatorname{Suff}(w)\}.}             \tag{1.2}
\]

#### Proof

Appending destroys no old interval.  Every new interval ends at the appended
cell and consists of a suffix of \(w\) followed by \(x\), so its OR is exactly
\(s\vee x\).  These are all new intervals.  QED.

Thus one-cell completion of an altered 12,873 basin is not heuristic: it is
the finite suffix-form condition (1.2).

## 2. Fixed-prefix one-append obstruction

The complete suffix-state set of the frozen 12,873 word is

\[
\begin{aligned}
\{&0,52289,52321,52323,52327,52455,\\
  &56551,64743,64751,65007,65519,65535\}.
                                                               \tag{2.1}
\end{aligned}
\]

### Theorem 2.1 (two appended cells are optimal for this fixed prefix)

No single appended nonzero cell completes the frozen 12,873 word.

#### Proof

To create \(0x287d\), the only suffix state in (2.1) contained in the target
is zero.  Hence (1.2) forces

\[
x=0x287d.                                                \tag{2.2}
\]

For \(0xce61\), the only contained suffix states are

\[
0,\quad0xcc41,\quad0xcc61,                            \tag{2.3}
\]

and each lacks bit \(0x0200\).  Therefore every appended witness for
\(0xce61\) requires \(0x0200\subseteq x\).  But

\[
0x0200\not\subseteq0x287d,                              \tag{2.4}
\]

contradicting (2.2).  QED.

The complete 65,535-cell census independently gives the gain histogram

\[
0^{65278},\qquad1^{129},\qquad2^{128},\qquad3^0.       \tag{2.5}
\]

Thus the displayed two-cell completion is cardinality-optimal among pure
appends to this exact prefix.  This is not a lower bound for altered prefixes
or internal exchanges.

## 3. The two-cell completion as a balanced exchange signature

The first appended cell pays the two high debts:

\[
0xcc61\vee0x0200=0xce61,
\qquad
0xcc63\vee0x0200=0xce63.                              \tag{3.1}
\]

The second pays the incompatible low debt as a singleton:

\[
0x287d=0x287d.                                         \tag{3.2}
\]

The obstruction (2.4) says these are genuinely different bit roles at the
current right boundary.  A length-12,874 construction must absorb one role
into the interior.  Equivalently, it must do one of the following.

1. Alter a 12,873 basin so all of its holes lie in one append fibre (1.2).
2. Start from a 12,874 one-hole basin and replace/rethread an internal cell so
   that \(0x287d\) is gained and every displaced target is recovered.
3. Delete a redundant cell from such a basin and use the freed length budget
   to append \(0x287d\), with the append simultaneously paying every deletion
   casualty.

This is the exact balanced-exchange interpretation of the two-cell
certificate.

## 4. Exact insertion and substitution interfaces

Fix a gap \(p\in\{0,\ldots,n\}\).  Let \(L_p\) be the ORs of suffixes of
\(w_0,\ldots,w_{p-1}\), including zero, and let \(R_p\) be the ORs of
prefixes of \(w_p,\ldots,w_{n-1}\), including zero.  Let
\(\mathcal D_p\) contain every target having no old witness entirely to one
side of the gap, together with every old hole.

### Theorem 4.1 (one-insertion iff)

Inserting \(x\) at gap \(p\) produces a universal word if and only if

\[
\boxed{
\mathcal D_p\subseteq
\{\ell\vee x\vee r:\ell\in L_p, r\in R_p\}.}         \tag{4.1}
\]

#### Proof

Every old witness wholly on one side survives.  Every other new witness must
contain the inserted cell and is uniquely a left suffix, \(x\), and a right
prefix.  QED.

For substitution at position \(p\), define \(L_p\) from the prefix ending at
\(p-1\), define \(R_p\) from the suffix beginning at \(p+1\), and let
\(\mathcal D_p\) be the targets with no old witness avoiding position \(p\),
together with the old holes.  The identical proof gives:

### Theorem 4.2 (one-substitution iff)

Replacing \(w_p\) by \(x\) produces a universal word if and only if

\[
\boxed{
\mathcal D_p\subseteq
\{\ell\vee x\vee r:\ell\in L_p, r\in R_p\}.}         \tag{4.2}
\]

In particular, if the only old hole is \(T\), every successful replacement
must have \(x\subseteq T\).  The other rows of \(\mathcal D_p\) are the exact
casualty bank; singleton target positivity is not enough.

The same statement has a useful support-two form.  For a target \(t\), let
\(\mathcal I_w(t)\) be its old provider intervals.  For positions \(p<q\),
let \(D_{p,q}(t)\) count the old providers meeting \(\{p,q\}\), and let
\(A_{p,q}^{x,y}(t)\) count the intervals meeting \(\{p,q\}\) whose OR is
\(t\) after the replacements.  Then the occurrence multiplicities satisfy
the exact identity

\[
c_{w'}(t)=c_w(t)-D_{p,q}(t)+A_{p,q}^{x,y}(t).          \tag{4.3}
\]

Indeed, providers avoiding both cells are unchanged, the other old providers
are precisely the \(D\)-term, and their complete replacement family is the
\(A\)-term.  In particular, put

\[
 \mathcal K_{p,q}=\mathcal H(w)\cup
 \{t:\text{every }I\in\mathcal I_w(t)
             \text{ meets }\{p,q\}\}.                 \tag{4.4}
\]

Let \(L_p\) be the left suffix-OR chain before \(p\), let \(A_{p,q}\) be
the prefix-OR chain of the unchanged open interval \((p,q)\), let
\(B_{p,q}\) be its suffix-OR chain, and let \(R_q\) be the right prefix-OR
chain after \(q\).  All four chains contain zero.  Finally put

\[
 M_{p,q}=\bigvee_{p<i<q}w_i.                           \tag{4.5}
\]

### Theorem 4.3 (exact two-cell exchange interface)

After replacing \(w_p,w_q\) by \(x,y\), respectively, the word is universal
if and only if

\[
\boxed{
\mathcal K_{p,q}\subseteq
 (L_p\vee x\vee A_{p,q})
 \cup(B_{p,q}\vee y\vee R_q)
 \cup(L_p\vee x\vee M_{p,q}\vee y\vee R_q).}          \tag{4.6}
\]

Here the join of sets of masks means all pointwise ORs.  The three terms in
(4.6) are exactly the new intervals containing \(p\) only, \(q\) only, or
both changed positions.  Every target outside \(\mathcal K_{p,q}\) keeps an
old provider avoiding both positions, while every target in
\(\mathcal K_{p,q}\) must use one of those three families.  This proves both
directions.

There is also a compact provider-span test for which rows can enter a
one-cell casualty bank.  If

\[
 a(t)=\max_{[i,j]\in\mathcal I_w(t)}i,
 \qquad b(t)=\min_{[i,j]\in\mathcal I_w(t)}j,          \tag{4.7}
\]

then every provider contains cell \(p\) exactly when
\(a(t)\le p\le b(t)\), and every provider crosses gap \(p\) exactly when
\(a(t)<p\le b(t)\).  Thus the complete private row family is obtained
without guessing witness priorities.

## 5. The new 12,874 one-hole basin

The word

```text
scratch/k16_ripple_insert12874_onehole.word
SHA-256 5ac147eca512b7e398c7217f1796836f454a304274c6e54fda7050fc9b4f66db
```

has length 12,874, covers exactly 65,534 nonzero masks, and has sole debt

\[
T=10365=0x287d.                                        \tag{5.1}
\]

Appending or prepending \(T\) completes it, but only at length 12,875.  The
complete insertion-kernel census has exactly these two solutions:

\[
(p,x)=(0,T),\qquad(12874,T),                           \tag{5.2}
\]

and no internal insertion.  More importantly for fixed length, the complete
one-substitution census is negative.

### Theorem 5.1 (exact one-cell local minimum)

Among all positions and all replacement literals capable of witnessing
\(T\), there are exactly 26,889 structurally capable substitution contexts
and no completion.  Every such substitution creates at least two uncovered
targets.  The minimum is attained in 169 contexts and has exactly four
position/casualty packets:

\[
\begin{array}{c|c|c|c}
p&w_p&\text{new casualty pair}&\text{replacement count}\\ \hline
0&0x882c&\{0xa86d,0xac6d\}&128\\
5921&0x2921&\{0x2939,0x293d\}&8\\
6440&0xa069&\{0xa879,0xa87d\}&32\\
12873&0xce41&\{0xce61,0xce63\}&1.
\end{array}                                             \tag{5.3}
\]

In the last row the replacement is forced to be \(T\).  Its action is the
exact boundary switch

\[
\boxed{
0xce41\longmapsto0x287d:quad
\text{gain }0x287d,quad
\text{lose }0xce61,0xce63.}                            \tag{5.4}
\]

The lost targets have unique old providers

\[
0xce61:[12872,12873],\qquad
0xce63:[12871,12873].                                  \tag{5.5}
\]

#### Proof of Theorem 5.1

Any new interval witnessing \(T\) contains the replacement cell, so its
literal is a nonzero submask of \(T\).  The audit examines all
\(12874(2^{|T|}-1)=3,282,870\) position/literal pairs, using the exact
left-suffix/right-prefix products in Theorem 4.2.  Exactly 26,889 can create
\(T\).  For each of them it recomputes every private target row and its new
local witnesses; none has an empty casualty bank, the minimum bank size is
two, and grouping all 169 minimizers by position and casualty set gives
(5.3).  A separate full ending-OR replay gives (5.4)--(5.5).  All counts and
hashes are fail-closed in the artifacts of Section 7.  QED.

An exact 2,412-context backup audit finds no nontrivial substitution at a
position \(p<12872\) which preserves all current coverage while creating
both terminal backups.  Therefore the most direct ordered architecture
"one safe earlier backup, then (5.4)" is closed.  This does **not** exclude a
simultaneous support-two exchange satisfying (4.6): its first edit may carry
a temporary debt which the second edit also repairs.

For the deletion-plus-append route, let \(v=w\setminus w_p\).  Appending
\(T\) can create only masks of the form

\[
T\vee s,\qquad s\in\operatorname{Suff}(v).           \tag{5.6}
\]

Hence every deletion casualty must contain \(T\), and must in fact be one
of the exact suffix forms (5.6).  This remains a strong solver-free
eligibility filter, but no complete deletion-plus-append no-go is claimed.

More generally, for any length-preserving preliminary edit \(E\), write

\[
G(E)=\operatorname{Cov}(w^E)\setminus\operatorname{Cov}(w),\qquad
L(E)=\operatorname{Cov}(w)\setminus\operatorname{Cov}(w^E). \tag{5.7}
\]

The post-edit hole set is exactly

\[
(\mathcal H(w)\setminus G(E))\cup L(E).                \tag{5.8}
\]

Thus a subsequent append by \(x\) succeeds if and only if the set (5.8)
lies in the suffix fibre of Theorem 1.1 for \(w^E\).  This is the exact
balance law behind every edit-plus-append attempt.

## 6. Relation to octahedral phase moves

The mixed octahedral \(C_6\) theorem acts on rank-eight carrier owners and
requires linked \(HH\), containment-cross, and \(LL\) edges.  The one-hole
word is an erosion/compiler cell stream; its top-bit runs do not authenticate
those owners or the fragment-to-byte map.  Therefore no literal C6 repair of
\(0x287d\) follows from the phase trace alone.

This is an audited provenance obstruction, not a mathematical nonexistence
theorem.  The exact edit ledger has nine equally minimum alignments with the
canonical lift, each using 197 substitutions, and records both
`byte_intrinsic_provenance_is_ambiguous=true` and
`external_invocation_or_checkpoint_found=false`.  No retained artifact maps
the emitted byte cells back to carrier owners and retained fragments.
Moreover the ripple cell-rank histogram is

\[
1^{24},\ 2^{164},\ 3^{635},\ 4^{1865},\
5^{5793},\ 6^{4387},\ 7^6,                            \tag{6.1}
\]

so no byte is itself a rank-eight carrier owner.

At the phase-trace level the word has tagged mass 6375 and 124 cyclic phase
boundaries.  For representative replacements in the four rows of (5.3), the
changes in `(tagged mass, cyclic boundaries)` are respectively

\[
(-1,0),\quad(0,0),\quad(-1,-2),\quad(-1,+2).          \tag{6.2}
\]

Thus the \(p=5921\) packet is the only minimum-casualty branch already
neutral in both scalar phase resources.  Its eight allowed literals are

\[
0x2861,0x2860,0x2061,0x2060,
0x0861,0x0860,0x0061,0x0060,                          \tag{6.3}
\]

and each trades the sole hole for \(\{0x2939,0x293d\}\).  This is the
sharpest support-two branch compatible with the scalar invariants of one
mixed octahedral cell.  Scalar compatibility is still far short of a literal
cell: an actual lift must supply the linked three-shore owner support, exact
shadow witnesses, and compiler provenance.

The familiar \(p=6440\) phase switch and the terminal switch (5.4) have
opposite boundary changes, so together they restore the boundary count.
They lose two units of tagged mass and leave all four debts

\[
\{0xa879,0xa87d,0xce61,0xce63\},                      \tag{6.4}
\]

and hence are not a mixed-\(C_6\) realization even at trace level.

If a carrier/compiler provenance map is later supplied, Theorem 4.2 is
the support-one ledger and Theorem 4.3 the support-two ledger that a
transparent C6 packet must satisfy: gain \(0x287d\), retain every avoiding
provider, and re-create every private casualty.  Until then, the proof-safe
finite target is the balanced word exchange (4.6), while the general K15
octahedral descent continues independently.

## 7. Frozen artifacts and scope

The lightweight fail-closed audit is

```text
scratch/audit_k16_append_one_interfaces_20260730.py
SHA-256 be7d6e1b01170cb307dde613ad50ec333a615a185232436e5e7cf5298ad1a032
```

with compact output

```text
scratch/k16_append_one_interfaces_20260730.audit.json
SHA-256 82fa8fa05e5c92a087f985dad3b0d733b5b6f37f328ef31d44a395f842ebd5c9
```

The complete insertion/substitution and phase-resource audit is

```text
scratch/audit_k16_12875_append_and_ripple_onecell_20260730.py
SHA-256 c6ab5e848265c8800f712f6682675ac91b6733bc5015430432fb8da801c753c9
scratch/k16_12875_append_and_ripple_onecell_20260730.audit.json
SHA-256 28c7ce8e22a6915af3262f1c3b4b7c641e9491ab54452e0cd2e9740a5c8f2b92
payload SHA-256 f1f1d2bb9a16f3dd4f87ecff00d7d872371d05107fdf28facfb22b9ad54dbdb4
```

The canonical-lift provenance ledger used in Section 6 is

```text
scratch/k16_12873_repaired_partial_exact_edit_ledger_20260730.audit.json
SHA-256 ae6b54352575bd6478291d6ef84dd8f0addf92e2a9f0e51af40fc2328a61e2fb
```

No heavy local search was run.  Existing remote optimal-length searches were
not duplicated.  The exact one-cell scans are lightweight compressed
provider audits.  This report proves fixed-prefix and interface theorems; it
does not claim a universal word of length 12,874 or 12,873, and it does not
exclude deletion, relocation, block reversal, or a simultaneous support-two
exchange.
