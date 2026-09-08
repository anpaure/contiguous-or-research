# Sixth-wave Y: the exact four-middle-set completion gate

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
B=\operatorname{Cat}_m=\frac Wn,
\]

and, for fixed \(A>0\),

\[
H=H_A=\lceil A\sqrt m\rceil.
\]

Take \(m\) sufficiently large that \(m\ge3\) and \(H\le m-1\).
All factors below are literal squarefree exact middle wreath factors.

This report does **not** prove \((\mathrm{SCC}_A)\) or
\((\mathrm{GCC}_A)\).  It proves two sharper exact obstructions at the
missing completion gate.

First, common lower overlap of two middle-disjoint wreaths is determined by
their union of middle supports.  If

\[
\mathcal I_0(R)\mathbin{\dot\cup}\mathcal I_0(D)
=\mathcal I_0(R')\mathbin{\dot\cup}\mathcal I_0(D'),
\]

then, simultaneously for every \(1\le q\le m-1\),

\[
\boxed{
\mathcal I_q(R)\cap\mathcal I_q(D)
=\mathcal I_q(R')\cap\mathcal I_q(D').
}
\tag{Y6.1}
\]

Thus every exact two-for-two repartition preserves every
\(h_q(R,D)\) and hence the full weighted overlap \(g_H(R,D)\).  Its two
partial sides also have exactly the same number of whole-fibre exact
completions.  Therefore a completion injection whose comparison statistic
is only the distinguished active-pair overlap cannot improve that statistic:
it changes neither completion multiplicity nor the active-pair overlap.  To
change that pair overlap itself, a comparison must change the \(2n\)-element
middle union and hence recruit at least one additional owner.  A fixed-union
two-for-two trade can still change its cross-overlaps with untouched rows;
this caveat is essential and is quantified in Section 2.1.

Second, depth one has an exact four-middle-set completion formula.  Fix an
\((m-1)\)-set \(S\) and four distinct elements \(a,b,c,d\notin S\).  Let

\[
e=\{S+a,S+b\},\qquad f=\{S+c,S+d\}
\]

be two vertex-disjoint Johnson edges with common intersection \(S\).  If
\(\mathscr C\) is an original heat communicating class, let

\[
r_{\mathscr C}
=\Pr_{F\sim\pi_{\mathscr C}}(f\text{ is selected}\mid
e\text{ is selected}).
\]

Then

\[
\boxed{
r_{\mathscr C}
=\frac{\displaystyle \frac4{m+2}
+\frac{\mathbb E_{\pi_{\mathscr C}}Q_1}{W}}
{\binom m2}.
}
\tag{Y6.2}
\]

The marginal probability of \(f\) is exactly

\[
p_m=\frac2{m(m+1)}.
\tag{Y6.3}
\]

Consequently the likelihood ratio

\[
\alpha_{\mathscr C}=\frac{r_{\mathscr C}}{p_m}
\]

satisfies

\[
\boxed{
\frac{\mathbb E_{\pi_{\mathscr C}}Q_1}{W}
=\frac{m-1}{m+1}\alpha_{\mathscr C}-\frac4{m+2}.
}
\tag{Y6.4}
\]

Therefore an \((\mathrm{SCC}_A)\)-scale class must obey

\[
\boxed{
\alpha_{\mathscr C}
\le
\frac{m+1}{m-1}
\left(\frac4{m+2}+\frac{C_AH_A}{n}\right)
=O_A(m^{-1/2}).
}
\tag{Y6.5}
\]

The identical statement holds for the uniform whole-fibre law under
\((\mathrm{GCC}_A)\).  This is much stronger than ordinary negative
association or a constant-factor completion comparison.  Exact completion
must make a prescribed second disjoint star edge a vanishing
\(O_A(m^{-1/2})\) fraction as likely as its already rare marginal.

The ratio in (Y6.5) is an average of literal row-pair completion ratios.
The candidate row pairs are middle-compatible except for an
\(O(1/m)\) fraction.  Hence pairwise middle exclusion cannot supply the
suppression: almost all already-compatible candidate pairs must themselves
form a completion desert.

These theorems close distinguished-pair-only repartitioning, one-row
completion homomesy, ordinary negative-dependence, and weak-contiguity
routes to \((\mathrm{SCC}_A)\)/\((\mathrm{GCC}_A)\).  They do not exclude
cross-term engineering by a fixed-union switch or a genuinely global
multiowner completion argument; those are part of the precise remaining
boundary.

---

## 1. Exact setup and the depth-one floor

Let \(\mathscr W_m\) be the set of unoriented wreaths, with

\[
M=|\mathscr W_m|=\frac{(n-1)!}{2}.
\]

For a wreath \(R\), let \(\mathcal I_0(R)\) be its \(n\) middle
\(m\)-intervals, and for \(q\ge1\), let \(\mathcal I_q(R)\) be its
\(n\) cyclic \((m-q)\)-intervals.

For an exact factor \(F\), define

\[
\mu_q^F(S)=|\{R\in F:S\in\mathcal I_q(R)\}|.
\]

For \(1\le q\le H\), put

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac{W}{N_q},\qquad
c_q=\lfloor\lambda_q\rfloor,
\tag{Y6.5a}
\]

and define the exact integer-floor excess

\[
Q_q(F)
=\sum_{S\in\binom{[n]}{m-q}}
\bigl(\mu_q^F(S)-c_q\bigr)
\bigl(\mu_q^F(S)-c_q-1\bigr),
\tag{Y6.5b}
\]

\[
\mathcal Q_H(F)=\sum_{q=1}^{H}\frac{Q_q(F)}{c_q}.
\tag{Y6.5c}
\]

Every summand in (Y6.5b) is a product of consecutive integers and is
therefore nonnegative.  These definitions retain the exact floors; no
quadratic relaxation is used.

At depth one,

\[
N_1=\binom n{m-1}=\frac{m}{m+2}W,
\qquad
\lambda_1=\frac W{N_1}=\frac{m+2}{m}.
\tag{Y6.6}
\]

Thus \(c_1=1\), and in the full-energy normalization

\[
Q_1(F)
=\sum_{S\in\binom{[n]}{m-1}}
(\mu_1^F(S)-1)(\mu_1^F(S)-2).
\tag{Y6.7}
\]

The exact integer pair floor is

\[
L_1=\frac{2W}{m+2},
\tag{Y6.8}
\]

and

\[
\sum_S\mu_1^F(S)(\mu_1^F(S)-1)=2L_1+Q_1(F).
\tag{Y6.9}
\]

Every original heat class \(\mathscr C\) is \(S_n\)-stable and has its
uniform law \(\pi_{\mathscr C}\) as stationary law.  For wreaths \(R,D\),
write

\[
d_{\mathscr C}(R)
=|\{F\in\mathscr C:R\in F\}|,
\]

\[
d_{\mathscr C}(R,D)
=|\{F\in\mathscr C:R,D\in F\}|.
\]

Class stability gives the exact one-row replication number

\[
d_{\mathscr C}(R)=d_{\mathscr C}
=\frac{|\mathscr C|B}{M}.
\tag{Y6.10}
\]

---

## 2. Two-owner middle-union rigidity at every depth

For \(|S|=m-q\), define

\[
a_{q,S}(R)
=|\{X\in\mathcal I_0(R):S\subseteq X\}|.
\tag{Y6.11}
\]

### Lemma 2.1: sharp single-row containment cap

For every wreath \(R\),

\[
\boxed{a_{q,S}(R)\le q+1,}
\tag{Y6.12}
\]

with equality exactly when \(S\in\mathcal I_q(R)\).

#### Proof

Complementation identifies middle intervals of \(R\) which contain \(S\)
with cyclic \((m+1)\)-intervals of \(R\) contained in
\([n]\setminus S\).  This complement has size

\[
m+q+1<2(m+1).
\]

Therefore at most one of its cyclic runs can have length at least
\(m+1\).  If that run has length \(u\), it contains
\(u-(m+1)+1\le q+1\) cyclic \((m+1)\)-intervals.  Equality requires the
run to have the full size \(m+q+1\), so the complement is one run and
\(S\) is the complementary cyclic \((m-q)\)-interval.  The converse is
immediate. \(\square\)

### Theorem 2.2: two-owner union saturation

Let \(R,D\) and \(R',D'\) be middle-disjoint wreath pairs satisfying

\[
\mathcal I_0(R)\mathbin{\dot\cup}\mathcal I_0(D)
=\mathcal I_0(R')\mathbin{\dot\cup}\mathcal I_0(D')
=:\mathcal U.
\tag{Y6.13}
\]

Then (Y6.1) holds for every \(q\).

#### Proof

For fixed \(S\), the union determines

\[
A_{q,S}(\mathcal U)
=|\{X\in\mathcal U:S\subseteq X\}|
=a_{q,S}(R)+a_{q,S}(D).
\tag{Y6.14}
\]

By Lemma 2.1, both summands are at most \(q+1\).  Thus

\[
S\in\mathcal I_q(R)\cap\mathcal I_q(D)
\iff A_{q,S}(\mathcal U)=2(q+1).
\tag{Y6.15}
\]

The right side depends only on \(\mathcal U\), and the same equivalence
applies to \(R',D'\). \(\square\)

For distinct wreaths put

\[
h_q(R,D)=|\mathcal I_q(R)\cap\mathcal I_q(D)|,
\qquad
g_H(R,D)=\sum_{q=1}^{H}\frac{h_q(R,D)}{c_q}.
\tag{Y6.16}
\]

Theorem 2.2 gives

\[
h_q(R,D)=h_q(R',D'),
\qquad
g_H(R,D)=g_H(R',D').
\tag{Y6.17}
\]

This is stronger than middle-support preservation: every common lower
target is preserved individually.

### 2.1 Whole-fibre completion factorization

Let \(\mathfrak F_m\) be the whole exact-factor fibre.  For a
\(2n\)-element middle union \(\mathcal U\), let

\[
\mathcal P(\mathcal U)
=\{\{R,D\}:\mathcal I_0(R)\dot\cup\mathcal I_0(D)=\mathcal U\}.
\]

Let \(\kappa(\mathcal U)\) be the number of exact wreath packings of the
middle complement \(\binom{[n]}m\setminus\mathcal U\).  For every
\(\{R,D\}\in\mathcal P(\mathcal U)\), adjoining such a complement is a
bijection onto exact factors containing \(R,D\).  Hence

\[
\boxed{
d_{\mathfrak F_m}(R,D)=\kappa(\mathcal U).
}
\tag{Y6.18}
\]

By Theorem 2.2, write the common pair overlap as \(g_H(\mathcal U)\).
Double counting a factor with a distinguished unordered row pair gives

\[
\boxed{
|\mathfrak F_m|\binom B2
=\sum_{\mathcal U}
\kappa(\mathcal U)|\mathcal P(\mathcal U)|,
}
\tag{Y6.19}
\]

and

\[
\boxed{
\sum_{F\in\mathfrak F_m}
\sum_{\{R,D\}\subset F}g_H(R,D)
=\sum_{\mathcal U}
\kappa(\mathcal U)|\mathcal P(\mathcal U)|g_H(\mathcal U).
}
\tag{Y6.20}
\]

Thus a two-for-two switch within one fixed \(\mathcal U\) is exactly
neutral with respect to its raw completion count and its active-pair
overlap.  In particular, it cannot suppress a comparison statistic which
charges only that distinguished pair in (Y6.20).

It need not be neutral for the full energy of an individual completed
factor.  If

\[
F'=\bigl(F\setminus\{R,D\}\bigr)\cup\{R',D'\}
\]

is exact and the two active pairs have the same middle union, then the
fixed total lower incidence and (Y6.17) give the exact identity

\[
\boxed{
\mathcal Q_H(F')-\mathcal Q_H(F)
=2\sum_{E\in F\setminus\{R,D\}}
\bigl(g_H(R',E)+g_H(D',E)-g_H(R,E)-g_H(D,E)\bigr).
}
\tag{Y6.20a}
\]

Thus a fixed-union two-row trade may improve the full energy entirely
through cross terms with untouched rows.  The theorem rules out only the
more local mechanism of changing the offending active pair or its raw
number of completions.

This conclusion is stated for whole-fibre counts.  A class-restricted
completion count need not be a function of \(\mathcal U\), because the
alternate decomposition need not lie in the same original heat class.

### 2.2 Exact buffer requirement for a multiowner switch

The same cap quantifies the first possible escape.  Let
\(\mathcal A,\mathcal B\) be two \(k\)-row middle packings with identical
middle incidence.  For fixed \((q,S)\), set

\[
t_{\mathcal A}
=|\{R\in\mathcal A:S\in\mathcal I_q(R)\}|,
\]

\[
\rho_{\mathcal A}
=\sum_{R\in\mathcal A}
\left(a_{q,S}(R)
-(q+1)\mathbf1_{\{S\in\mathcal I_q(R)\}}\right),
\tag{Y6.21}
\]

and similarly for \(\mathcal B\).  Equality of the middle unions gives

\[
\boxed{
(q+1)t_{\mathcal A}+\rho_{\mathcal A}
=(q+1)t_{\mathcal B}+\rho_{\mathcal B}.
}
\tag{Y6.22}
\]

Suppose \(d=t_{\mathcal A}-t_{\mathcal B}\ge0\), and put
\(b=k-t_{\mathcal A}\).  The new side has \(b+d\) nonlower rows, each
with restitution at most \(q\), so

\[
(q+1)d
=\rho_{\mathcal B}-\rho_{\mathcal A}
\le q(b+d)-\rho_{\mathcal A}.
\]

Therefore

\[
\boxed{d\le qb-\rho_{\mathcal A}.}
\tag{Y6.23}
\]

At depth one, a nonlower row has restitution zero or one.  Every unit by
which a trade lowers the number of owners of \(S\) therefore requires an
old buffer row which owns no middle superset of \(S\).  In particular,
two active lower owners with no buffer cannot have their collision removed
by any two-for-two exact switch.

---

## 3. The exact depth-one star matching

Every wreath orders its \(n\) middle windows cyclically.  Consecutive
windows differ by one Johnson exchange, so an exact factor \(F\) gives a
spanning \(2\)-factor

\[
G_1(F)\subset J(n,m),
\tag{Y6.24}
\]

which is the disjoint union of its \(B\) wreath cycles.  It has exactly
\(W\) edges.

Fix \(S\in\binom{[n]}{m-1}\) and put

\[
T=[n]\setminus S,\qquad |T|=m+2.
\]

The Johnson edges with intersection \(S\) are naturally the edges of the
complete graph \(K_T\): the edge \(\{x,y\}\) represents

\[
\{S\cup\{x\},S\cup\{y\}\}.
\]

Define \(\mathcal M_S(F)\) to be the selected edges of \(G_1(F)\) with
intersection \(S\).

### Lemma 3.1: literal matching model

The set \(\mathcal M_S(F)\) is a matching on \(T\), and

\[
\boxed{|\mathcal M_S(F)|=\mu_1^F(S).}
\tag{Y6.25}
\]

#### Proof

If two selected color-\(S\) edges shared the vertex \(S\cup\{x\}\), that
middle set would have two selected color-\(S\) incidences in the unique
wreath cycle which owns it.  But the two edges of a sliding-window cycle
at one middle window delete its two distinct endpoints, so their
\((m-1)\)-intersections are distinct.  Thus the color class is a matching.

A wreath contributes one color-\(S\) edge exactly when \(S\) is its cyclic
\((m-1)\)-interval: the edge joins the two middle windows obtained by
extending \(S\) at its two ends.  This proves (Y6.25). \(\square\)

### Theorem 3.2: exact four-middle-set likelihood

Let \(\mathscr C\) be an original heat class and let
\(Z_S=|\mathcal M_S(F)|\) under \(F\sim\pi_{\mathscr C}\).  For a fixed
edge \(e\subset T\),

\[
\boxed{
\Pr(e\in\mathcal M_S)=p_m=\frac2{m(m+1)}.
}
\tag{Y6.26}
\]

For fixed disjoint edges \(e,f\subset T\), equation (Y6.2) holds.

#### Proof

Class \(S_n\)-stability and target transitivity give

\[
\mathbb EZ_S=\lambda_1=\frac{m+2}{m}.
\tag{Y6.27}
\]

The stabilizer of \(S\) is transitive on the

\[
K=\binom{m+2}{2}
\]

edges of \(K_T\), so \(Kp_m=\lambda_1\), proving (Y6.26).

It is also transitive on ordered pairs \((e,f)\) of disjoint edges.  Once
\(e\) is fixed, there are

\[
L=\binom m2
\]

possible \(f\).  Therefore

\[
\mathbb E[Z_S(Z_S-1)]
=KL\Pr(e,f\in\mathcal M_S)
=\lambda_1Lr_{\mathscr C}.
\tag{Y6.28}
\]

On the other hand, (Y6.7) and target transitivity give

\[
\frac{\mathbb E Q_1}{N_1}
=\mathbb E[(Z_S-1)(Z_S-2)]
=\mathbb E[Z_S(Z_S-1)]-2(\lambda_1-1).
\tag{Y6.29}
\]

Since \(\lambda_1-1=2/m\) and \(N_1\lambda_1=W\), substitution of
(Y6.28) into (Y6.29) gives

\[
\mathbb E Q_1
=WLr_{\mathscr C}-\frac{4W}{m+2},
\tag{Y6.30}
\]

which is (Y6.2). \(\square\)

Equivalently,

\[
\boxed{
\mathbb E Q_1
=W\binom m2(r_{\mathscr C}-r_0),
\qquad
r_0=\frac8{m(m-1)(m+2)}.
}
\tag{Y6.31}
\]

The ordinary integer floor \(Q_1\ge0\) is precisely

\[
\alpha_{\mathscr C}\ge
\frac{4(m+1)}{(m-1)(m+2)}.
\tag{Y6.32}
\]

### Corollary 3.3: exact SCC-scale necessary condition

If

\[
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H\le C_AH_AB,
\tag{Y6.33}
\]

then \(Q_1\le\mathcal Q_H\), and (Y6.4) gives (Y6.5).  In particular,
any lower bound

\[
\alpha_{\mathscr C}\ge\eta_m,
\qquad
\eta_m\gg m^{-1/2},
\tag{Y6.34}
\]

rules out (Y6.33) for that class.  A fixed positive lower bound forces
\(\mathbb E Q_1=\Omega(W)\).

Conversely, merely proving ordinary negative association

\[
r_{\mathscr C}\le p_m
\]

only gives \(\mathbb E Q_1=O(W)\), which is larger than
\(H_AB=O_A(W/\sqrt m)\) by a factor \(\Theta_A(\sqrt m)\).  The required
upper bound is the vanishing ratio (Y6.5), not a constant-factor
correlation estimate.

There is also an exact local concentration consequence.  Since

\[
(z-1)(z-2)\ge2\mathbf1_{\{z\notin\{1,2\}\}}
\qquad(z\in\mathbb Z_{\ge0}),
\]

(Y6.29) and (Y6.33) imply

\[
\boxed{
\Pr(Z_S\notin\{1,2\})
\le
\frac{C_AH_A(m+2)}{2nm}
=O_A(m^{-1/2}).
}
\tag{Y6.35}
\]

This is a necessary statement about the literal star matching in a low
stationary class, not an independently proved concentration theorem.

---

## 4. Literal row-completion expansion

Let \(\mathscr R_e\) be the set of wreaths whose middle-window cycle uses
the fixed Johnson edge \(e\).

### Lemma 4.1: exact edge multiplicity

\[
\boxed{
|\mathscr R_e|=a_m=(m-1)!m!.
}
\tag{Y6.36}
\]

#### Proof

Place the \((m-1)\)-set \(S\) as one ordered block and the remaining
\(m\) elements of \(T\setminus e\) as the complementary ordered block.
The two elements of \(e\) occupy the two boundary positions.  There are
\((m-1)!m!\) resulting unoriented cyclic orders: exchanging the two
boundary elements is exactly cancelled by reversing the cyclic order.
\(\square\)

For disjoint \(e,f\), unique middle ownership gives

\[
d_{\mathscr C}(e)=a_md_{\mathscr C},
\tag{Y6.37}
\]

\[
d_{\mathscr C}(e,f)
=\sum_{R\in\mathscr R_e}
\sum_{D\in\mathscr R_f}d_{\mathscr C}(R,D).
\tag{Y6.38}
\]

Thus

\[
\boxed{
r_{\mathscr C}
=\frac{
\displaystyle\sum_{R\in\mathscr R_e}
\sum_{D\in\mathscr R_f}d_{\mathscr C}(R,D)}
{a_md_{\mathscr C}}.
}
\tag{Y6.39}
\]

Define the literal pair-likelihood ratio relative to independent class row
marginals by

\[
\ell_{\mathscr C}(R,D)
=\frac{|\mathscr C|d_{\mathscr C}(R,D)}{d_{\mathscr C}^2}.
\tag{Y6.40}
\]

Since

\[
\frac{a_mB}{M}=p_m,
\tag{Y6.41}
\]

equations (Y6.39)--(Y6.41) give

\[
\boxed{
\alpha_{\mathscr C}
=\frac1{a_m^2}
\sum_{R\in\mathscr R_e}
\sum_{D\in\mathscr R_f}\ell_{\mathscr C}(R,D).
}
\tag{Y6.42}
\]

Every term in (Y6.42) is a literal squarefree exact-factor completion
ratio.  There is no signed or fractional state.

For direct comparison with the uniform \(B\)-subset benchmark, put

\[
p_*=\frac{B-1}{M-1},
\qquad
\gamma_m=\frac{M(B-1)}{B(M-1)},
\tag{Y6.43}
\]

and

\[
\widetilde{\mathscr L}_{\mathscr C}
=\frac1{a_m^2}
\sum_{R\in\mathscr R_e}
\sum_{D\in\mathscr R_f}
\frac{d_{\mathscr C}(R,D)}{d_{\mathscr C}p_*}.
\tag{Y6.44}
\]

Then

\[
\boxed{
\alpha_{\mathscr C}=\gamma_m
\widetilde{\mathscr L}_{\mathscr C},
}
\tag{Y6.45}
\]

and the exact completion-count form of (Y6.4) is

\[
\boxed{
\frac{\mathbb E Q_1}{W}
=\gamma_m\frac{m-1}{m+1}
\widetilde{\mathscr L}_{\mathscr C}
-\frac4{m+2}.
}
\tag{Y6.46}
\]

In particular, (Y6.33) forces

\[
\boxed{
\widetilde{\mathscr L}_{\mathscr C}
\le
\gamma_m^{-1}\frac{m+1}{m-1}
\left(\frac4{m+2}+\frac{C_AH_A}{n}\right)
=O_A(m^{-1/2}).
}
\tag{Y6.47}
\]

### 4.1 Middle-compatible completion desert

The independently audited overlap bound from the preceding Y5 report says
that two independent uniform wreaths conditioned to contain \(S\) as a
lower interval are middle-incompatible with probability at most \(13/m\).
Their two boundary edges in \(K_T\) are disjoint with probability

\[
\frac{\binom m2}{\binom{m+2}{2}}
=\frac{m(m-1)}{(m+2)(m+1)}.
\]

The stabilizer of \(S\) is transitive on ordered disjoint boundary-edge
pairs.  Therefore the fraction of pairs in
\(\mathscr R_e\times\mathscr R_f\) which are middle-incompatible is at most

\[
\boxed{
\varepsilon_m
=\frac{13(m+2)(m+1)}{m^2(m-1)}
=O(m^{-1}).
}
\tag{Y6.48}
\]

For every incompatible pair, \(d_{\mathscr C}(R,D)=0\).  Since all terms
in (Y6.42) are nonnegative, (Y6.5) and (Y6.48) imply

\[
\boxed{
\frac1{|\mathscr K_{e,f}|}
\sum_{(R,D)\in\mathscr K_{e,f}}
\ell_{\mathscr C}(R,D)
=O_A(m^{-1/2}),
}
\tag{Y6.49}
\]

where \(\mathscr K_{e,f}\) is the set of middle-compatible pairs in
\(\mathscr R_e\times\mathscr R_f\).  Thus the required vanishing
likelihood persists after all pairwise-forbidden rows have been deleted.

### 4.2 Fixed-edge conditional spill

Condition on \(e\in\mathcal M_S(F)\).  The remaining \(m\) star vertices
are either paired into one of the \(Z_S-1\) companion edges or owned as a
noninterval singleton by another row.  Hence the literal distinguished-edge
spill is

\[
\sigma_e(F)=m-2(Z_S-1).
\tag{Y6.50}
\]

Using \(\mathbb E[Z_S-1\mid e]=Lr_{\mathscr C}\) and (Y6.30),

\[
\boxed{
\mathbb E[\sigma_e\mid e]
=m-\frac8{m+2}-2\frac{\mathbb E Q_1}{W}.
}
\tag{Y6.51}
\]

Therefore (Y6.33) requires this fixed-edge spill mean to lie within

\[
\frac{2C_AH_A}{n}=O_A(m^{-1/2})
\tag{Y6.52}
\]

of the formal floor-compatible ceiling \(m-8/(m+2)\).  This is the local
version of the aggregate spill gate: after fixing one literal selected
adjacency, almost every remaining star middle set must be absorbed by a
noninterval owner.

---

## 5. Single-wreath completion homomesy is powerless

The four-middle-set ratio is the first genuinely cross-wreath statistic.
All consecutive completion data confined to one selected wreath segment
are class-independent.

For \(1\le\ell\le m\), let \(\mathscr P_\ell\) be the oriented sequences

\[
P=(X_0,X_1,\ldots,X_\ell)
\]

of middle sets which occur as consecutive windows of an oriented wreath.

### Theorem 5.1: exact path homomesy

For every nonempty \(S_n\)-stable family \(\mathscr C\) of exact factors
and every fixed \(P\in\mathscr P_\ell\),

\[
\boxed{
\frac{|\{F\in\mathscr C:P\text{ occurs in }G_1(F)\}|}{|\mathscr C|}
=\frac2{(m)_\ell(m+1)_\ell}.
}
\tag{Y6.53}
\]

#### Proof

Such a path is uniquely specified by its initial middle set \(X_0\), an
ordered \(\ell\)-tuple of distinct elements removed from \(X_0\), and an
ordered \(\ell\)-tuple of distinct elements added from its complement.
Thus

\[
|\mathscr P_\ell|=W(m)_\ell(m+1)_\ell,
\tag{Y6.54}
\]

and \(S_n\) is transitive on \(\mathscr P_\ell\).

Every exact factor contains exactly \(2nB=2W\) such oriented paths: each
of its \(B\) wreath cycles supplies \(n\) starting points and two
directions.  They are distinct because different wreaths have disjoint
middle supports.  Transitivity now gives (Y6.53). \(\square\)

At \(\ell=1\), (Y6.53) is the edge marginal (Y6.26).  At \(\ell=2\), it
also fixes the conditional probability of every prescribed compatible
second edge incident with the same middle vertex:

\[
\Pr(\text{second incident edge}\mid\text{first edge})
=\frac1{m(m-1)}.
\tag{Y6.55}
\]

Thus no one-edge, one-middle-vertex, or even half-cycle one-wreath
completion statistic can distinguish a low-energy heat class.  The two
edges in (Y6.2) are vertex-disjoint and must lie in distinct wreaths; their
conditional completion ratio is the first free statistic in this hierarchy.

There is a literal exact-factor witness to the strength of this no-go.
The independently audited marked-gap theorem for the canonical MSW exact
factor gives

\[
Q_1(F_m^{\rm MSW})\ge(1/8-o(1))W.
\tag{Y6.56}
\]

Its uniform coordinate orbit is an \(S_n\)-stable family of literal exact
factors, so it satisfies every path homomesy (Y6.53), while (Y6.4) gives

\[
\alpha_{\rm MSW}\ge1/8-o(1).
\tag{Y6.57}
\]

This orbit law is **not** asserted to be stationary for the original heat:
the MSW transposition overlays have fragmented component cells.  Its role
is precise.  Literal exactness, full coordinate invariance, the exact
middle cover, and every single-wreath path marginal still do not imply the
cross-wreath suppression (Y6.5).

---

## 6. Exact proved/conditional boundary

The following statements are proved unconditionally.

1. **All-depth two-owner rigidity.**  Common lower overlap of a
   middle-disjoint pair is a function of its middle union, by (Y6.15).

2. **Active-pair completion neutrality.**  In the whole fibre, every
   two-row decomposition of one middle union has the same raw completion
   count and the same active-pair \(g_H\), by (Y6.18)--(Y6.20).  Its
   cross-overlaps with the complementary rows may change, exactly as in
   (Y6.20a).

3. **Buffer necessity.**  A multiowner same-union trade lowering a
   depth-\(q\) owner multiplicity must satisfy the exact inequality
   (Y6.23).

4. **Four-middle-set identity.**  For every original heat class, the first
   floor energy is exactly the conditional probability in (Y6.2), or the
   literal row-completion average in (Y6.42)/(Y6.46).

5. **Compatible completion desert required.**  Any SCC-scale class must
   satisfy (Y6.49); pairwise middle incompatibility accounts for only an
   \(O(1/m)\) fraction of the candidate row pairs.

6. **One-wreath no-go.**  All fixed consecutive path marginals through
   length \(m\) are exactly class-independent, and an actual exact-factor
   orbit satisfying them can still have \(Q_1=\Omega(W)\).

What remains unproved is exactly the needed positive estimate

\[
\min_{\mathscr C}\alpha_{\mathscr C}=O_A(m^{-1/2}),
\tag{Y6.58}
\]

together with the analogous simultaneous controls at depths
\(2\le q\le H_A\).  Equation (Y6.58) is necessary, not sufficient, for
\((\mathrm{SCC}_A)\).  Replacing the minimum by the uniform whole-fibre
ratio gives the corresponding necessary depth-one gate for
\((\mathrm{GCC}_A)\).

The new obstruction is definitive for the distinguished-pair-only route:
no completion-count injection which only repartitions the two offending
owners can change either the active pair's completion multiplicity or its
own overlap.  A proof may still exploit the cross terms in (Y6.20a).
Otherwise, to change the active collision itself it must compare different
middle unions and use at least one genuine buffer owner.  In every case it
must ultimately prove the vanishing four-middle-set likelihood rather than
an \(O(1)\) negative-dependence estimate.

No assertion here proves \((\mathrm{SCC}_A)\), \((\mathrm{GCC}_A)\), MWB,
or the constant-one contiguous-OR theorem.

---

## 7. Independent audit checklist

The decisive identities were checked in the following independent forms.

* The cap \(a_{q,S}\le q+1\) was proved by complementary cyclic runs; the
  saturation value \(2(q+1)\) then proves (Y6.1) target by target.

* The matching marginal was checked both from
  \(\mathbb EZ_S=(m+2)/m\) and from the exact edge count
  \(|E(J(n,m))|=Wm(m+1)/2\).

* The four-edge formula was checked both by the factorial moment
  \(\mathbb E[Z_S(Z_S-1)]\) and by the global ordered collision count
  \(2L_1+\mathbb EQ_1\).

* The row multiplicity \((m-1)!m!\), the identity
  \(a_mB/M=2/[m(m+1)]\), and every normalization in
  (Y6.39)--(Y6.47) were recomputed separately.

* The compatibility correction (Y6.48) conditions the audited \(13/m\)
  bound on the exact disjoint-boundary probability
  \(m(m-1)/[(m+2)(m+1)]\).

* The implication scale uses
  \(H_AB/W=H_A/n=O_A(m^{-1/2})\), and nothing stronger.

The whole-union factorization is deliberately not promoted to a
class-specific identity, the MSW orbit is deliberately not called
stationary, and the necessary four-edge estimate is deliberately not
called a proof of SCC or GCC.
