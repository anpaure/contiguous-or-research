# Central PBBS, stopped ordinary annulus, and product-SCD tail: exact synthesis audit

Date: 2026-07-27

Method: pure mathematics only. No finite search, computation, solver, or web
input is used.

## 0. Verdict

Put

\[
 W_e=\binom{2m}{m},\qquad W_o=\binom{2m+1}{m}.
\]

The presently proved central and exterior constructions do **not** have a
common economical cutoff:

\[
 \text{PBBS central: }h=o(\sqrt m),
 \qquad
 \text{product-SCD exterior: }H/\sqrt m\longrightarrow\infty.
\tag{0.1}
\]

The exact stopped-profile annulus does not yet fill this gap. It proves an
identity for the defect of one ordinary entrance matching, but it does not
prove the required little-oh estimate. More importantly, even an unrestricted
proof of that estimate would produce a second annular body unless its
successor letters are physically identified with positions already paid for
in the PBBS/core word.

After fixing that common-body requirement, the smallest missing numerical
assertion is the following. For every fixed \(0<a<b\), choose one common even
projection, one PBBS-compatible family \(\mathcal A\) of strongly correct
starts, one integral grouping into ordinary packets, and one common history
family, with

\[
 q_0=a\sqrt m+O(1),\qquad H=b\sqrt m+O(1),\qquad
 G=|\mathcal A|,\qquad L=N_{q_0}-G.
\]

Then one needs

\[
\boxed{
 \begin{aligned}
 &\sum_{\sigma\in\{-,+\}}\sum_{q=q_0}^{H}
 \left(
   \min\{G,N_q\}
   -\left|\{\Theta_q^\sigma(A):A\in\mathcal A\}\right|
 \right)
 +Q^\sharp=o(W_e),
 \end{aligned}}
\tag{CB--SP}
\]

where \(N_q=\binom{2m}{m-q}=\binom{2m}{m+q}\), and \(Q^\sharp\)
is the signed, all-depth incidence expansion of every history altered or
discarded after selection. In the undeleted complement-equivariant case the
two signed sums agree, and the lower sum is exactly equation (5.5) of
`MATH_OBSTRUCTION_N_ANNULAR_NESTED_LOAD_TELESCOPING_20260727.md`.

Assertion (CB--SP), with its common-body and common-projection quantifiers, is
**unproved**. The stopped-profile martingale proves only an exact identity
whose right-hand side would imply (CB--SP) if it were shown to be little-oh.
Consequently the current results do not prove the constant-one conjecture.

The rest of this note proves every deterministic estimate needed for the
conditional synthesis and audits parity lift and deletion.

## 1. The two proved endpoint ranges

### Proposition 1.1 (quantitative central range)

For \(1\le h\le\sqrt m\), the audited PBBS compiler gives in odd dimension
\(2m+1\) a literal word covering

\[
 [m-h,m+h+1]
\]

of length

\[
 W_o+O(W_o h/\sqrt m).
\tag{1.1}
\]

In particular this is \(W_o+o(W_o)\) whenever \(h=o(\sqrt m)\).
There is also an even-dimensional word of length

\[
 W_e+O(W_e h/\sqrt m)
\tag{1.2}
\]

covering every target in

\[
 [m-h,m+h].
\tag{1.3}
\]

#### Proof

The proved dominance-staircase ledger is

\[
 \mathcal L_h\le W_o+2h\operatorname{Cat}_m
       +2(5h-1)\nu_h(P_m),
\]

up to the harmless one-unit indexing convention recorded in the central-band
theorem, and the proved monotone packing estimate is

\[
 \nu_h(P_m)=O(\operatorname{Cat}_m\sqrt m)
 \qquad(h\le\lceil\sqrt m\rceil).
\]

Since \(W_o=(2m+1)\operatorname{Cat}_m\), division by \(W_o\) gives
(1.1). This is the quantitative form used below; for a fixed
\(h=a\sqrt m\) it gives excess \(O(aW_o)\), not little-oh.

For the even statement apply the odd construction with parameter \(m-1\)
on \(2m-1\) coordinates and use the exact trimmed one-coordinate lift. A
target of rank \(k\) avoiding the new coordinate is covered when

\[
 m-1-h\le k\le m+h,
\]

and a target containing it is covered when its deletion has rank \(k-1\)
in that interval. Both kinds are therefore covered simultaneously for
\(m-h\le k\le m+h\). The lift doubles the length, while

\[
 \binom{2m}{m}=2\binom{2m-1}{m-1}.
\]

This proves (1.2)--(1.3). \(\square\)

### Proposition 1.2 (sharp exterior quantifier)

For every \(0\le H\le m-1\), the even product-SCD word has exact length

\[
 L_m(m-H-1)
\]

and covers all nonempty targets of ranks

\[
 |S|\le m-H-1\quad\text{or}\quad |S|\ge m+H+1.
\tag{1.4}
\]

Its audited asymptotic quantifier is

\[
 \frac{L_m(m-H-1)}{W_e}=o(1)
 \quad\Longleftrightarrow\quad
 \frac H{\sqrt m}\longrightarrow\infty.
\tag{1.5}
\]

Uniformly,

\[
 L_m(m-H-1)\le C W_e e^{-H^2/(8m)}.
\tag{1.6}
\]

At \(H=A\sqrt m+o(\sqrt m)\), with fixed finite \(A\), the normalized
length tends to a strictly positive value \(F(A)\).

#### Proof

These are exactly the literal coverage, exact-length, uniform upper-bound,
and converse statements proved and audited in
`MATH_ATTACK_N_PRODUCT_SCD_TAIL_UNIFORM_ASYMPTOTIC_20260726.md` and
`MATH_AUDIT_PRODUCT_SCD_TAIL_EXACT_GAUSSIAN_QUANTIFIER_20260726.md`.
They are quoted here as proved inputs. \(\square\)

Propositions 1.1 and 1.2 prove that no single cutoff is currently economical
for both mechanisms. A cutoff \(o(\sqrt m)\) makes the tail \(\Theta(W_e)\),
and a cutoff \(\omega(\sqrt m)\) lies outside the proved coefficient-one
central range.

## 2. What the stopped-profile annulus proves

Fix for the moment constants \(0<a<b\), and put

\[
 q_0=a\sqrt m+O(1),\qquad H=b\sqrt m+O(1),\qquad D=H-q_0,
\]

\[
 N_d=\binom{2m}{m-q_0-d}\qquad(0\le d\le D).
\]

Let one ordinary entrance matching have the same occurrence mass \(G\) at
every depth, and let \(S_d\) be its distinct lower-target support at depth
\(d\). Set

\[
 L=N_0-G,
\]

\[
 B(L)=\sum_{d=0}^{D}(N_d-G)_+,
\qquad
 \mathfrak C=\sum_{d=0}^{D}
 \bigl(\min\{G,N_d\}-|S_d|\bigr).
\tag{2.1}
\]

The proved pathwise identity is

\[
 \sum_{d=0}^{D}H_d=B(L)+\mathfrak C.
\tag{2.2}
\]

Complementation gives the same upper bill. If a stopped bite process is
used, its proved martingale identity is

\[
 \mathbb E\mathfrak C_\tau
 =\mathbb E\sum_{j<\tau}\mathscr P_j,
\tag{2.3}
\]

where \(\mathscr P_j\) retains the exact selected-incidence and same-bite
coalescence terms. Thus the missing stochastic estimate is

\[
 \mathbb E\sum_{j<\tau}\mathscr P_j=o(W_e).
\tag{SP}
\]

Neither (SP) nor \(\mathfrak C=o(W_e)\) is proved in
`MATH_THEOREM_ORDINARY_ANNULAR_STOPPED_PROFILE_FUNCTIONAL_20260727.md`.
That note is an exact reduction, not an existence theorem. Its fixed
\((a,b)\) formulation is nevertheless sufficient for a later diagonal:
uniformity in \(a,b\) would not be required if the theorem were proved for
each fixed pair.

### Lemma 2.1 (uniform scalar-leave estimate)

Let \(0\le q_0\le H<m\),

\[
 N_d=\binom{2m}{m-q_0-d},\qquad
 G=(1-\delta)N_0,qquad 0\le\delta\le\tfrac12.
\]

Then, for every terminal depth \(D\le H-q_0\),

\[
\boxed{
 B(L)\le N_0\delta\bigl(1+2\sqrt{m\delta}\bigr).}
\tag{2.4}
\]

Consequently

\[
 L=O(N_0/\sqrt m)\quad\Longrightarrow\quad
 B(L)=O(W_e m^{-1/4})=o(W_e),
\tag{2.5}
\]

uniformly in \(q_0\) and \(H\). In particular the scalar leave remains
harmless when \(q_0=o(\sqrt m)\) and \(H/\sqrt m\to\infty\).

#### Proof

The exact consecutive ratio is

\[
 \frac{N_{d+1}}{N_d}
 =\frac{m-q_0-d}{m+q_0+d+1}.
\]

For \(q_0+d\le H<m\), use \(\log(1-x)\le-x\) and
\(m+q_0+d+1\le2m\) to obtain

\[
 \begin{aligned}
 \log\frac{N_d}{N_0}
 &\le -\sum_{j=0}^{d-1}
       \frac{2q_0+2j+1}{m+q_0+j+1}\\
 &\le-\frac1{2m}\sum_{j=0}^{d-1}(2j+1)
 =-\frac{d^2}{2m}.
 \end{aligned}
\tag{2.6}
\]

If the depth-\(d\) summand in \(B(L)\) is positive, then

\[
 e^{-d^2/(2m)}\ge\frac{N_d}{N_0}>1-\delta.
\]

Since \(-\log(1-\delta)\le2\delta\) for
\(0\le\delta\le1/2\), this forces

\[
 d<2\sqrt{m\delta}.
\]

There are at most \(1+2\sqrt{m\delta}\) such integer depths, and every
positive summand is at most

\[
 N_0-G=N_0\delta.
\]

This proves (2.4). If \(\delta=O(m^{-1/2})\), then its right-hand side is
\(O(N_0m^{-1/4})\), and \(N_0\le W_e\), proving (2.5). \(\square\)

Thus the scalar term \(B(L)\) is not the missing overlap.

## 3. Why an unrestricted annulus is not a fusion

### Lemma 3.1 (a separately paid entrance body has Gaussian width)

Every literal word whose internal intervals cover all
rank-\((m-q_0)\) targets has length at least

\[
 N_0=\binom{2m}{m-q_0}.
\tag{3.1}
\]

For \(q_0=a\sqrt m+O(1)\), fixed \(a\ge0\),

\[
 \frac{N_0}{W_e}=e^{-a^2+o(1)}.
\tag{3.2}
\]

Hence a standalone annulus body costs \(\Theta(W_e)\); along a diagonal
\(a\to0\) it costs \((1-o(1))W_e\).

#### Proof

Choose one witnessing interval for every entrance target and assign the
target to the right endpoint of that interval. For a fixed right endpoint,
the unions obtained by moving the left endpoint are nested. Two distinct
sets of the same cardinality cannot be strictly nested, so at most one
entrance target is assigned to each word position. This proves (3.1).

Also

\[
 \frac{N_0}{W_e}
 =\prod_{i=1}^{q_0}\frac{m-i+1}{m+i}.
\]

For \(q_0=O(\sqrt m)\), Taylor expansion with a uniform summed remainder
gives

\[
 \begin{aligned}
 \log\frac{N_0}{W_e}
 &=-\sum_{i=1}^{q_0}\frac{2i-1}{m}
   +O\left(\frac{q_0}{m}+\frac{q_0^3}{m^2}\right)\\
 &=-\frac{q_0^2}{m}+o(1)=-a^2+o(1).
 \end{aligned}
\]

This proves (3.2). \(\square\)

Lemma 3.1 does not prohibit a nonlocal overlay. It proves that merely
constructing a good annular packet word and concatenating it with the PBBS
word pays a second positive-density baseline. Cross-seam windows can add
witnesses, but no current theorem supplies the required systematic reuse.

The exact successful interface is Theorem 5.2 of
`MATH_THEOREM_DOMINO_TWIN_ANNULUS_PBBS_COMMON_LEAVE_INTERFACE_20260727.md`.
Its indispensable first hypothesis is:

> the successor letters of the annular paths are the same physical letters
> already charged in the PBBS/core body, and the annular flags are suffix
> flags of those letters.

The current PBBS theorem supplies only coverage. Its pointwise support
quantifier is of the form

\[
 \forall q\ \forall S\ \exists A=A(q,S),
\tag{3.3}
\]

whereas fusion needs one common projection and one family satisfying

\[
 \exists\mathcal A\ \forall q.
\tag{3.4}
\]

Although each strongly correct PBBS fan can be extended individually to an
ordinary packet after deleting an unused coordinate, that coordinate may
depend on the fan. Pointwise extension therefore does not furnish a common
even projection, packetization, or entrance histogram. This is the exact
quantifier gap behind (CB--SP).

## 4. Exact deterministic fusion ledger

Assume now, as an explicitly **unproved common-body hypothesis**, that the
PBBS/core and the ordinary annular histories use the same physical successor
letters and preserve all already charged inner witnesses. Let the selected
states be cut into \(p\) legal paths. The proved hard-started path compiler
and (2.2) give the exact additional bound

\[
 \boxed{
 2B(L)+2\mathfrak C+Q^\sharp+2Hp.}
\tag{4.1}
\]

Here

\[
 Q^\sharp=
 \sum_{\sigma\in\{-,+\}}\sum_{d=0}^{D}
 |\operatorname{tr}^{\sigma}_d(\mathcal Q_0)|_{\rm inc}
\tag{4.2}
\]

is the incidence count after expanding every altered or quarantined entrance
history through every annular depth. If only the number of entrance histories
is known, the safe deterministic estimate is

\[
 Q^\sharp\le2(D+1)|\mathcal Q_0|.
\tag{4.3}
\]

Thus \(|\mathcal Q_0|=o(W_e)\) is not sufficient. At Gaussian width the
structure-free condition is \(|\mathcal Q_0|=o(W_e/\sqrt m)\), and at a
growing cutoff it is \(o(W_e/H)\).

For full ordinary packets, cutting each packet once gives

\[
 p\le \frac{G}{2m}=O(W_e/m).
\tag{4.4}
\]

Therefore

\[
 2Hp=O(HW_e/m)=o(W_e)
\tag{4.5}
\]

whenever \(H=o(m)\). Lemma 2.1 disposes of \(B(L)\). Hence, inside an
already constructed common body, the remaining numerical condition is

\[
 \mathfrak C+Q^\sharp=o(W_e),
\tag{4.6}
\]

with both shores understood. This is (CB--SP).

## 5. Deletion audit

There are two different deletion interfaces and they must not be conflated.

### 5.1 Exact-factor row deletion

For an exact middle factor \(F\), the proved product-SCD consumer uses

\[
 J_H(F)=\sum_{q=1}^{H}\frac{O_q(F)}{c_q}.
\]

If \(R\) complete factor rows are deleted, its factor-independent sufficient
condition is

\[
 J_H(F)=o(W_o),qquad
 R=o(\operatorname{Cat}_m/\sqrt m).
\tag{5.1}
\]

More generally an occurrence-deletion vector \(\delta_q\) is safely handled
by

\[
 \sum_{q=1}^{H}\frac{\|\delta_q\|_1}{c_q}=o(W_o),
\tag{5.2}
\]

together with an \(o(W_o)\) middle leave and an actual retained Stage-A word
of length \(W_o+o(W_o)\).

The stopped entrance leave

\[
 L=O(W_e/\sqrt m)
\]

cannot simply be inserted into a size-only floor-buffer estimate: multiplying
it by the available \(O(\sqrt m)\) reciprocal-capacity sum gives only
\(O(W_e)\), not little-oh. Nor is \(L\) a count of complete factor rows.

### 5.2 Actual-defect composition

The product-SCD exterior is factor-blind. Once the final central word and its
actual holes have been accounted for, it may be concatenated without any
endpoint, owner, or deletion compatibility. Thus the correct stopped-annulus
interface is the actual-defect ledger

\[
 B(L)+\mathfrak C+Q^\sharp=o(W_e),
\tag{5.3}
\]

not the size-only row corollary. The tail's blindness does not repair central
holes; it only says that central switching or deletion cannot invalidate the
separate exterior witnesses.

## 6. Parity lift audit

Suppose first that a complete even universal word \(U\) has been constructed,
including central band, annulus, and exterior, with

\[
 |U|=W_e+o(W_e).
\]

For one new coordinate \(z\), the exact trimmed lift

\[
 U_1,\ldots,U_N,\{z\},
 U_1\cup\{z\},\ldots,U_{N-1}\cup\{z\}
\]

has length \(2N\) and is universal on \(2m+1\) coordinates. Indeed, old
targets retain their witnesses; a target \(S\cup\{z\}\) uses the transformed
copy of a witness for \(S\), except that a witness ending at \(U_N\) uses
the old suffix followed by \(\{z\}\).

Since

\[
 W_o=\frac{2m+1}{m+1}W_e,
 \qquad
 \frac{2W_e}{W_o}=1+\frac1{2m+1},
\tag{6.1}
\]

the lifted length is \(W_o+o(W_o)\). An \(o(W_e)\) defect or edit ledger
also remains little-oh after the factor-two lift.

The order of operations matters: lift the completed even common-body word
once. Separately lifting a PBBS word and an unrelated annulus word does not
create the missing common-body chronology.

## 7. Conditional constant-one synthesis

### Theorem 7.1 (conditional diagonal consumer)

Assume the following **unproved theorem** for every fixed pair
\(0<a<b\): there is a PBBS-compatible common-body ordinary packet family
on \([2m]\) satisfying

1. one common even projection, one integral packetization, and literal
   common-successor chronology;
2. \(L=O_{a,b}(N_0/\sqrt m)\);
3. (CB--SP), including every post-selection alteration through
   \(Q^\sharp\);
4. a full-packet path cover, hence \(p=O(W_e/m)\);
5. installation in the quantitative PBBS core with no more than
   \(o_{a,b}(W_e)\) additional inner-witness damage.

Then

\[
 \nu(k)\le(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\tag{7.1}
\]

#### Proof

Let

\[
 a_j=1/j,qquad b_j=j.
\]

For fixed \(j\), apply the assumed theorem at \((a_j,b_j)\). Choose a
threshold \(M_j\) beyond which its normalized little-oh errors are at most
\(1/j\). Now choose an integer \(j=j(m)\to\infty\) so slowly that

\[
 m\ge M_{j(m)},\qquad j(m)=o(\sqrt m).
\]

Put

\[
 q_0=\left\lceil\frac{\sqrt m}{j}\right\rceil,
 \qquad h=q_0-1,
 \qquad H=\lceil j\sqrt m\rceil.
\tag{7.2}
\]

The even rank ranges partition exactly as follows:

\[
\begin{array}{ll}
\text{central:}&[m-q_0+1,m+q_0-1],\\
\text{annulus:}&[m-H,m-q_0]\cup[m+q_0,m+H],\\
\text{exterior:}&[0,m-H-1]\cup[m+H+1,2m].
\end{array}
\tag{7.3}
\]

By Proposition 1.1 the normalized PBBS excess is \(O(1/j)\). By
Lemma 2.1 and the assumed (CB--SP), the annular hole/quarantine bill is
little-oh along the chosen diagonal. By (4.5),

\[
 \frac{2Hp}{W_e}=O(j/\sqrt m)=o(1).
\]

Finally (1.6) gives exterior normalized length at most

\[
 C e^{-j^2/8}=o(1).
\]

The exact common-body ledger (4.1), followed by the separate exterior,
therefore gives an even universal word of length \(W_e+o(W_e)\). Section 6
then gives the odd case. \(\square\)

## 8. Authoritative proved/conditional boundary

The following parts are proved and quantitatively compatible:

1. the PBBS central word through every \(h=o(\sqrt m)\);
2. the product-SCD exterior with little-oh cost exactly for
   \(H/\sqrt m\to\infty\);
3. the exact stopped-profile identities (2.2)--(2.3);
4. the uniform scalar estimate (2.4);
5. the reset estimate \(2Hp=o(W_e)\) for full packets and \(H=o(m)\);
6. the expanded-deletion ledger \(Q^\sharp\), the exact-factor deletion
   alternatives, and the factor-blind exterior composition; and
7. the one-time parity lift.

The following are not proved:

1. (SP), even in the unrestricted ordinary packet catalogue;
2. the stronger PBBS-compatible common-family inequality (CB--SP);
3. one common even projection and integral ordinary packetization for the
   required PBBS starts; and
4. a physical common-body embedding preserving the already paid central
   witnesses.

An adversarial check shows why none may be suppressed:

- fixed-depth PBBS surjectivity has the wrong quantifier order for a nested
  all-depth family;
- an individually available deleted coordinate need not be common across
  fans;
- balanced marginals and time-zero codegrees do not control the
  hole-labelled stopped drift;
- \(o(W_e)\) deleted roots can expand to \(\Theta(W_e)\) target incidences;
- a separately compiled entrance layer already costs
  \((e^{-a^2}+o(1))W_e\); and
- the trimmed lift preserves a fusion but cannot manufacture one.

Accordingly, the exact stopped-profile annulus supplies the correct defect
functional and closes the scalar-leave accounting, but it does **not** yet
supply the missing overlap. The minimal remaining theorem is (CB--SP) inside
one genuinely shared PBBS/core chronology.

