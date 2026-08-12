# All-form CHHM voltage--Euler components at the middle layer

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 T={W\over n}=\operatorname {Cat}_m.
\tag{0.1}
\]

The proposed transition-form route has a clean exact ledger, but the
published Curtis--Hines--Hurlbert--Moyer transition catalogue does not give
the desired component improvement in the central regime.

There are exactly \(T\) circular-gap form classes of \(m\)-subsets of
\(\mathbb Z_n\).  This statement is valid for composite \(n\): because

\[
                         \gcd(n,m)=1,
\tag{0.2}
\]

every middle translation orbit is free and every positive gap composition
of \(n\) into \(m\) parts is aperiodic under cyclic rotation.

If a quotient Euler circuit \(D\) uses \(\ell(D)\) form classes and has
total voltage \(v(D)\in\mathbb Z_n\), its physical lift consists of exactly

\[
 \boxed{g(D)=\gcd(n,v(D))}
\tag{0.3}
\]

singleton-Ucycle components, each of length

\[
 \boxed{{n\ell(D)\over g(D)}.}
\tag{0.4}
\]

Thus an all-form quotient decomposition has

\[
 \boxed{
 C_{\rm lift}=\sum_Dg(D),\qquad
 {W\over C_{\rm lift}}
 ={n\sum_D\ell(D)\over\sum_Dg(D)}.}
\tag{0.5}
\]

The exact wreath factor already gives \(C=T=W/n=\Theta(W/m)\) components
of length \(n=\Theta(m)\).  Therefore the new rotor target is not the
existence of a length-\(\Theta(m)\) factor.  It is the strict improvement

\[
 \sum_Dg(D)=o(T),
\tag{0.6}
\]

equivalently average lifted length \(\omega(m)\).  The stronger proposed
bound

\[
                         C_{\rm lift}=O(W/m^2)=O(T/m)
\tag{0.7}
\]

requires quotient circuits with weighted average

\[
                         {\sum_D\ell(D)\over\sum_Dg(D)}
                         =\Omega(m).
\tag{0.8}
\]

In particular, long quotient circuits do not suffice at composite \(n\):
their voltage gcds enter with the exact weight (0.3).

The central bad-class obstruction is quantitative.  There is an absolute
constant \(\delta>0\) such that, for all sufficiently large \(m\), at least

\[
                         \boxed{\delta T}
\tag{0.9}

form classes have no gap size of multiplicity one.  They are non-good and
hence non-awesome.  The published CHHM transition-form Euler graph lists
the awesome forms; it supplies no transition option for the classes in
(0.9).

Consequently, any augmentation in which every quotient circuit contains
at most \(K\) bad forms satisfies

\[
 \boxed{C_{\rm lift}\ge {\delta T\over K}.}
\tag{0.10}
\]

Even granting every bad form an ideal unit-voltage singleton quotient loop
gives \(C_{\rm lift}\ge\delta T=\Omega(W/m)\).  Thus a bounded local
completion of the published catalogue cannot prove (0.6).  To prove merely
\(o(W/m)\), the average number of bad forms per lifted component must tend
to infinity.  To prove (0.7), it must be \(\Omega(m)\), after division by
the voltage gcd:

\[
 \boxed{
 {\sum_D b(D)\over\sum_Dg(D)}=\Omega(m),}
\tag{0.11}
\]

where \(b(D)\) is the number of bad forms on \(D\).

No theorem currently supplies the transitions needed for (0.11).  The
result is therefore a sharp negative audit of the **published**
transition-form lead, not an impossibility theorem for a new all-form
transition system.

There is also an independent prefix gate.  Component count and voltage do
not imply that the shorter symbol windows cover ranks
\(m-1,\ldots,m-H\).  After quotienting translations, prefix coverage is an
additional collection of integral orbit-incidence inequalities using the
same rooted form choices.  At composite \(n\), lower targets may have
nontrivial stabilizers; the exact multiplicity is their stabilizer order,
but the cover condition itself is still one condition per lower
translation orbit.  Such periodic targets are exponentially sparse in a
fixed Gaussian window, and the raw prefix supply/demand ratio at
\(q=A\sqrt m\) tends to \(e^{A^2}\).  Hence there is no marginal prefix
deficit; the remaining gate is simultaneous integral incidence.

The exact surviving theorem is an all-form colored circulation with three
simultaneous requirements:

1. select one legal rooted transition option for every form class;
2. make the selected options Eulerian with
   \(\sum_D\gcd(n,v(D))=o(T)\); and
3. cover every lower prefix orbit through the Gaussian depth with those
   same integral choices.

This is strictly stronger than the CHHM awesome-form theorem and strictly
stronger than the exact wreath factor.

## 1. Free form classes for every \(n=2m+1\)

Let \(S\in\binom{\mathbb Z_n}{m}\).  List its members cyclically and write
its positive gap composition

\[
 d(S)=(d_1,\ldots,d_m),
 \qquad d_i\ge1,qquad \sum_i d_i=n.
\tag{1.1}
\]

Changing the distinguished member of \(S\) cyclically rotates (1.1), and
translating \(S\) leaves its cyclic form unchanged.

### Lemma 1.1 (middle translation orbits are free)

Every \(m\)-subset of \(\mathbb Z_n\) has trivial translation stabilizer.

#### Proof

Suppose a nontrivial translation subgroup \(H\le\mathbb Z_n\), of order
\(h>1\), stabilizes \(S\).  Every \(H\)-orbit on \(\mathbb Z_n\) has
cardinality \(h\), so \(S\) is a union of such orbits and \(h\mid m\).
Also \(h\mid n\), contradicting \(\gcd(n,m)=1\). \(\square\)

### Lemma 1.2 (every central gap composition is cyclically aperiodic)

No positive composition of \(n\) into \(m\) parts has a nontrivial cyclic
period.

#### Proof

If the composition consists of \(r>1\) repetitions of one shorter block,
then \(r\mid m\) and its total sum makes \(r\mid n\), again contradicting
(0.2). \(\square\)

There are \(\binom{n-1}{m-1}\) rooted positive gap compositions.  Lemma
1.2 puts exactly \(m\) of them in every cyclic form.  Hence the number of
forms is

\[
 {1\over m}\binom{n-1}{m-1}
 ={1\over n}\binom nm
 =T.
\tag{1.2}
\]

Lemma 1.1 says that every one of these forms represents exactly \(n\)
physical middle subsets.  No primality hypothesis on \(n\) occurs.

## 2. Exact voltage lifting, including composite \(n\)

Fix a section choosing one physical representative above every quotient
form state.  Give a directed quotient transition edge its translation
voltage in \(\mathbb Z_n\).

### Theorem 2.1 (voltage component formula)

Let \(D\) be a directed quotient circuit of length \(\ell\) and total
voltage

\[
                         v=\sum_{e\in D}\nu(e)\pmod n.
\tag{2.1}
\]

Its complete physical lift has \(g=\gcd(n,v)\) components, each of length
\(n\ell/g\).

#### Proof

After one traversal of \(D\), a lift beginning in phase \(a\in\mathbb Z_n\)
ends in phase \(a+v\).  The translation \(a\mapsto a+v\) has exactly
\(g=\gcd(n,v)\) orbits, each of length \(n/g\).  Following one such phase
orbit traverses \(D\) exactly \(n/g\) times and hence has physical length
\(n\ell/g\).  The \(g\) phase orbits partition all lifts. \(\square\)

The convention includes \(v=0\), for which \(\gcd(n,0)=n\): a zero-voltage
quotient circuit lifts to \(n\) physical circuits of the same length.

### Proposition 2.2 (cycle voltage is gauge invariant)

Changing the chosen representative of each quotient state does not change
the total voltage of a quotient circuit.

#### Proof

If the section at quotient vertex \(u\) is shifted by
\(a(u)\in\mathbb Z_n\), the voltage of an edge \(u\to v\) changes by the
coboundary

\[
                         \nu'(u,v)=\nu(u,v)+a(u)-a(v).
\tag{2.2}
\]

The additional terms telescope around every circuit. \(\square\)

Thus an unfavorable composite gcd cannot be repaired after the quotient
circuits have been chosen merely by rotating their representatives.  One
must change transition edges or the circuit decomposition itself.

Suppose the quotient circuits partition all \(T\) form classes, so

\[
                         \sum_D\ell(D)=T.
\tag{2.3}
\]

Theorem 2.1 gives (0.5) immediately.  It also gives the exact hierarchy

\[
 \begin{array}{c|c|c}
 \text{quotient circuit}&\text{lifted components}&
                         \text{lifted component length}\\ \hline
 v=0&n&\ell\\
 \gcd(n,v)=g&g&n\ell/g\\
 v\in\mathbb Z_n^\times&1&n\ell.
 \end{array}
\tag{2.4}
\]

Long unit-voltage circuits are optimal for the component ledger.  Long
zero-voltage circuits can still be poor, especially when \(\ell=O(n)\).

## 3. Positive density of bad odd-central forms

Call a positive gap composition **good** if some part size occurs exactly
once.  A CHHM-awesome composition has, in addition, a uniquely occurring
part greater than one.  Every non-good composition is non-awesome.

### Theorem 3.1 (positive-density bad forms at \(n=2m+1\))

There is an absolute \(\delta>0\) such that, for all sufficiently large
\(m\), at least a \(\delta\)-fraction of the positive compositions of
\(2m+1\) into \(m\) parts have no part size of multiplicity one.
Consequently at least \(\delta T\) cyclic form classes are non-good.

#### Proof

Let \(X_1,\ldots,X_m\) be independent with

\[
                         \Pr(X_i=r)=2^{-r},\qquad r\ge1.
\tag{3.1}
\]

Conditional on \(\sum_iX_i=2m+1\), their vector is the uniform positive
composition, because every such vector has probability \(2^{-(2m+1)}\).

Fix a sufficiently large constant \(C\), put

\[
 J=\lfloor\log_2m\rfloor-C,qquad q=2^{-J},
\tag{3.2}
\]

and condition first on \(E=\{X_i\le J\ \forall i\}\).  The probability of
\(E\) is \((1-q)^m\), bounded below by a positive constant depending only
on \(C\).  Under \(E\), the variables remain independent with truncated
law

\[
 \Pr(Y=r)={2^{-r}\over1-q},\qquad1\le r\le J,
\tag{3.3}
\]

mean

\[
                         \mu_J=2-{Jq\over1-q},
\tag{3.4}
\]

uniformly positive variance, uniformly bounded third moment, and lattice
span one.  The target differs from its mean by

\[
 2m+1-m\mu_J=1+{Jmq\over1-q}=O(\log m)=o(\sqrt m).
\tag{3.5}
\]

The lattice local central limit theorem for this truncated triangular
array therefore gives

\[
                         \Pr\left(\sum_iY_i=2m+1\right)
                         \ge {c_0\over\sqrt m}
\tag{3.6}
\]

for an absolute \(c_0>0\).

Let \(N_r\) count the occurrences of \(r\).  The expected occupancies of
the largest permitted values grow geometrically away from the cap:

\[
 m\Pr(Y=J-s)\ge2^{C+s}\qquad(s\ge0).
\tag{3.7}
\]

Consequently

\[
                         \sum_{r=1}^{J}\Pr(N_r=1)=:\eta_C
                         \longrightarrow0
\tag{3.8}
\]

as \(C\to\infty\), uniformly in \(m\).  To retain this estimate on the
local event in (3.6), expose the unique coordinate on \(\{N_r=1\}\).  The
remaining \(m-1\) truncated variables, conditioned not to equal \(r\),
have uniformly positive variance and largest atom bounded away from one.
The lattice concentration inequality therefore gives, uniformly in \(r\),

\[
 \Pr\left(N_r=1,\sum_iY_i=2m+1\right)
 \le {C_1\over\sqrt m}\Pr(N_r=1).
\tag{3.9}
\]

Choose \(C\) so that \(C_1\eta_C<c_0/2\).  Equations (3.6)--(3.9) yield

\[
 \Pr\left(\sum_iY_i=2m+1, N_r\ne1\ \forall r\right)
 \ge {c_0\over2\sqrt m}.
\tag{3.10}
\]

Multiplying by \(\Pr(E)\) and comparing with

\[
 \Pr\left(\sum_iX_i=2m+1\right)
 =2^{-(2m+1)}\binom{2m}{m-1}
 =\Theta(m^{-1/2})
\tag{3.11}
\]

shows that the conditional probability of no singleton multiplicity is
bounded below by an absolute positive constant.  The property is invariant
under cyclic rotation, and every form has exactly \(m\) rootings by Lemma
1.2, so the same fraction bound holds for cyclic forms. \(\square\)

This is the odd-central analogue of the even-central obstruction in
`CENTRAL_NEAR_UCYCLE.md`.  The one-unit change in the conditioned total
appears only in (3.5) and does not affect the local-CLT argument.

## 4. Why bounded completion of the CHHM catalogue fails

The published CHHM transition graph uses a distinguished uniquely
occurring nonunit gap to define its transition form and lists precisely the
awesome subset classes.  The non-good forms in Theorem 3.1 have no such
distinguished gap and are absent from that graph.

Suppose a new all-form quotient decomposition retains the published
awesome circuits and adds circuits which collectively contain the bad
forms.  Let \(b(D)\) be the number of bad forms on circuit \(D\), and put
\(g(D)=\gcd(n,v(D))\).  Since every lifted circuit contributes \(g(D)\ge1\)
components,

\[
 C_{\rm lift}=\sum_Dg(D)
 \ge\#\{D:b(D)>0\}.
\tag{4.1}
\]

If \(b(D)\le K\) for every circuit, Theorem 3.1 gives

\[
 C_{\rm lift}
 \ge {\sum_Db(D)\over K}
 \ge {\delta T\over K},
\tag{4.2}
\]

which is (0.10).

More generally,

\[
 {\sum_Db(D)\over C_{\rm lift}}
 ={\sum_Db(D)\over\sum_Dg(D)}
\tag{4.3}
\]

is the average number of bad quotient forms per lifted physical component,
with voltage splitting charged correctly.  Conditions (0.6)--(0.7) force
this ratio to tend to infinity or to be \(\Omega(m)\), respectively.

The optimistic singleton-loop audit is immediate.  Even if every bad form
were granted a legal quotient loop of unit voltage, it would contribute one
physical component.  Equation (0.9) would still give
\(C_{\rm lift}\ge\delta T\).  Actual CHHM transition forms do not grant
these loops; the calculation deliberately gives the local completion more
freedom than is presently proved.

Thus “include the bad classes” is not a marginal cleanup.  Almost all bad
classes must participate in long common Euler circuits, and those circuits
must simultaneously have small voltage gcd.

## 5. Exact all-form colored circulation

The missing theorem can be written without assuming a particular extension
of the transition catalogue.

Let \(\mathcal F\) be the \(T\) cyclic form classes.  Let \(V\) be a set of
transition states.  For every form \(F\), let \(\mathcal E_F\) be its legal
rooted transition options.  An option \(e\in\mathcal E_F\) has

* a tail \(t(e)\in V\);
* a head \(h(e)\in V\);
* a voltage \(\nu(e)\in\mathbb Z_n\); and
* for every \(q\le H\), a lower prefix form \(p_q(e)\) of size \(m-q\).

Choose variables \(x_e\in\{0,1\}\).  The exact owner-form and Euler
constraints are

\[
 \sum_{e\in\mathcal E_F}x_e=1
 \qquad(F\in\mathcal F),
\tag{5.1}
\]

\[
 \sum_{e:t(e)=v}x_e-\sum_{e:h(e)=v}x_e=0
 \qquad(v\in V).
\tag{5.2}
\]

An integral solution decomposes into directed Euler circuits \(D\).  Its
exact physical component objective is

\[
 \boxed{
 \Psi(x,\mathcal D)
 =\sum_{D\in\mathcal D}\gcd\!\left(
      n,\sum_{e\in D}\nu(e)\right).}
\tag{5.3}
\]

The circuit decomposition matters when one balanced directed component has
several possible Euler tours: different tours use the same edge multiset
and hence have the same total voltage on that connected Eulerian component,
but splitting it into smaller circuits changes the separate gcd sum.  The
minimum in (5.3) is therefore taken over Euler decompositions consistent
with the selected arcs.

The published CHHM catalogue supplies \(\mathcal E_F\ne\varnothing\) for
awesome forms.  It does not supply the option sets for the positive-density
bad family in (0.9).  Constructing those sets with sufficient cross-form
connectivity is the first new theorem required.

The fractional balance system associated with (5.1)--(5.2) has the exact
potential dual

\[
 \boxed{
 \sum_{F\in\mathcal F}
 \max_{e\in\mathcal E_F}
 \bigl(\phi(h(e))-\phi(t(e))\bigr)\ge0
 \quad(\phi:V\to\mathbb R).}
\tag{5.4}
\]

This follows directly from Farkas' lemma.  It is necessary and sufficient
for fractional Euler balance.  It says nothing by itself about the
nonlinear voltage-gcd objective (5.3), and it cannot even be evaluated on a
bad form until new legal options are supplied.

## 6. Prefix coverage and composite target stabilizers

Fix \(q\le H\) and a lower target

\[
                         Q\in\binom{\mathbb Z_n}{m-q}.
\]

Its translation stabilizer has order

\[
 h(Q)=|\operatorname {Stab}(Q)|,
 \qquad h(Q)\mid\gcd(n,m-q).
\tag{6.1}
\]

Indeed, if a subgroup of order \(h\) stabilizes \(Q\), then \(Q\) is a
union of its \(h\)-element orbits.  Thus \(h\mid n\) and \(h\mid m-q\).
Unlike the middle layer, lower layers can therefore have nonfree orbits
when \(n\) is composite.

Let \(\mathscr O_q\) be the lower translation-orbit set.  A single quotient
prefix occurrence of orbit type \(O\in\mathscr O_q\), lifted through all
\(n\) phases, covers every physical target in \(O\); each is obtained with
multiplicity exactly \(h(O)\).  Hence coverage, as opposed to balanced
multiplicity, is equivalent to

\[
 \boxed{
 \sum_{F}\sum_{\substack{e\in\mathcal E_F:\ p_q(e)=O}}x_e\ge1
 \qquad(O\in\mathscr O_q).}
\tag{6.2}
\]

There is no hidden positive-density loss from the composite stabilizers.
Indeed, a nonfree target is stabilized by a subgroup of some order
\(d\ge3\) dividing both \(n\) and \(m-q\), and is then a union of
\(d\)-element subgroup orbits.  For a fixed \(d\), there are at most

\[
                         \binom{n/d}{(m-q)/d}\le 2^{n/d}
\tag{6.3}
\]

such targets.  Since a cyclic group has one subgroup of each divisor
order, summing over divisors gives only \(2^{n/3+o(n)}\) nonfree targets.
Uniformly for \(q\le A\sqrt m\), Burnside's lemma therefore gives

\[
 |\mathscr O_q|
 ={1\over n}\binom{n}{m-q}+2^{-\Omega(m)}\binom{n}{m-q}.
\tag{6.4}
\]

The raw quotient-prefix supply-to-demand ratio is consequently

\[
 {T\over|\mathscr O_q|}
 =(1+o(1)){\binom{n}{m}\over\binom{n}{m-q}}
 =(1+o(1))
   \prod_{i=1}^{q}{m+1+i\over m-q+i}.
\tag{6.5}
\]

For \(q=A\sqrt m+O(1)\), this tends to \(e^{A^2}\), since

\[
 \log {\binom{n}{m}\over\binom{n}{m-q}}
 ={q^2+q\over m}+O\!\left({q^3\over m^2}\right).
\tag{6.6}
\]

Thus prefix coverage has the correct marginal capacity throughout every
fixed Gaussian window.  The unresolved issue is not a stabilizer or total
count deficit; it is simultaneous integral surjectivity of (6.2) under the
same port-balance and favorable-voltage choices.

The same variables must satisfy (6.2) for every
\(q=1,\ldots,H\).  Neither the Euler equations (5.2) nor favorable circuit
voltages imply these prefix inequalities.

For Gaussian \(H=A\sqrt m\), the system (6.2) contains all the simultaneous
shadow information missing from a middle-only near-Ucycle factor.  A proof
of the component theorem followed by an independent per-depth choice would
not suffice: rerooting one form changes its Euler ports, its voltage, and all
its prefixes together.

## 7. What the exact wreath factor does and does not prove

The exact wreath factor is a complete singleton-window factor of the middle
layer with

\[
                         C_{\rm wreath}=T={W\over n}
\tag{7.1}
\]

components, each of length \(n\).  It proves, uniformly and without a
primality assumption,

\[
                         {W\over C_{\rm wreath}}=n=\Theta(m).
\tag{7.2}
\]

It does **not** prove any of the following.

1. It does not give average component length \(\omega(m)\).
2. Its components are cyclic intervals in chosen coordinate orders and
   generally cut across the fixed-translation circular-gap classes.  It is
   not a one-component-per-form CHHM voltage decomposition.
3. Middle factorhood does not imply (6.2) at any positive depth.
4. Exact complement symmetry of each wreath does not improve the component
   count; the anti-dihedral rigidity theorem shows that preserving that
   symmetry during fusion forces the factor back to wreaths.

Thus the all-form transition lead is genuinely new only if it improves
(7.1) by an unbounded factor and simultaneously satisfies (6.2).

## 8. Exact remaining boundary

The proved implications are:

\[
 \boxed{
 \text{all-form quotient Euler decomposition}
 \Longrightarrow
 C_{\rm lift}=\sum_D\gcd(n,v(D)).}
\tag{8.1}
\]

\[
 \boxed{
 \text{published awesome-form transitions}
 +\ \text{bounded bad-form completion}
 \Longrightarrow
 C_{\rm lift}=\Omega(W/m).}
\tag{8.2}
\]

The exact sufficient theorem still missing is:

> **All-form voltage--Euler prefix theorem — unproved.**  Supply legal
> transition options for every one of the \(T\) form classes, including the
> positive-density non-good family, and select one option per class so that
> (5.2) and every Gaussian prefix constraint (6.2) hold, while the selected
> Euler components satisfy
> \[
>                         \sum_D\gcd(n,v(D))=o(T).
> \]
> For the quantitative bound \(O(W/m^2)\), replace the right side by
> \(O(T/m)\).

The class-size and composite-voltage audits introduce no hidden middle
stabilizer obstruction.  The obstruction is constructive and integral:
the known transition catalogue omits \(\Theta(T)\) forms, those forms must
be transported in growing bundles on favorable-voltage circuits, and the
same rooted choices must realize every lower prefix orbit.
